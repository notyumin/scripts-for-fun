package main

import (
	"encoding/json"
	"errors"
	"fmt"
	"net/http"
	"os"
	"strings"

	"github.com/charmbracelet/bubbles/list"
	"github.com/charmbracelet/bubbles/spinner"
	"github.com/charmbracelet/bubbles/textinput"
	tea "github.com/charmbracelet/bubbletea"
	"github.com/charmbracelet/lipgloss"
)

func main() {
	err := tea.NewProgram(initialModel(), tea.WithAltScreen()).Start()
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
}

func initialModel() Model {
	t := textinput.NewModel()
	t.Focus()

	s := spinner.NewModel()
	s.Spinner = spinner.Points

	return Model{
		textInput: t,
		spinner:   s,
		typing:    true,
	}
}

type Model struct {
	textInput textinput.Model
	spinner   spinner.Model
	list      list.Model

	typing   bool
	loading  bool
	err      error
	dicEntry DicEntry
}

type DicEntry []struct {
	Word      string `json:"word"`
	Phonetics []struct {
		Audio     string `json:"audio"`
		SourceURL string `json:"sourceUrl,omitempty"`
		License   struct {
			Name string `json:"name"`
			URL  string `json:"url"`
		} `json:"license,omitempty"`
		Text string `json:"text,omitempty"`
	} `json:"phonetics"`
	Meanings []struct {
		PartOfSpeech string `json:"partOfSpeech"`
		Definitions  []struct {
			Definition string        `json:"definition"`
			Synonyms   []interface{} `json:"synonyms"`
			Antonyms   []interface{} `json:"antonyms"`
		} `json:"definitions"`
		Synonyms []string      `json:"synonyms"`
		Antonyms []interface{} `json:"antonyms"`
	} `json:"meanings"`
	License struct {
		Name string `json:"name"`
		URL  string `json:"url"`
	} `json:"license"`
	SourceUrls []string `json:"sourceUrls"`
}

type GotDef struct {
	Err      error
	DicEntry DicEntry
}

func (m Model) fetchDicEntry(word string) tea.Cmd {
	return func() tea.Msg {
		url := fmt.Sprintf("https://api.dictionaryapi.dev/api/v2/entries/en/%s", word)
		res, err := http.Get(url)
		if err != nil {
			return GotDef{
				Err: err,
			}
		}

		var def DicEntry
		decodeErr := json.NewDecoder(res.Body).Decode(&def)
		if decodeErr != nil {
			return GotDef{
				Err: errors.New("No definitions found"),
			}
		}

		return GotDef{
			DicEntry: def,
		}
	}
}

func (m Model) Init() tea.Cmd {
	return textinput.Blink
}

func (m Model) Update(msg tea.Msg) (tea.Model, tea.Cmd) {
	switch msg := msg.(type) {
	case tea.KeyMsg:
		switch msg.String() {
		case "ctrl+c":
			return m, tea.Quit

		case "enter":
			if m.typing {
				word := strings.TrimSpace(m.textInput.Value())
				if word != "" {
					m.typing = false
					m.loading = true
					return m, tea.Batch(
						spinner.Tick,
						m.fetchDicEntry(word),
					)
				}
			}

		case "esc":
			if !m.typing && !m.loading {
				m.typing = true
				m.err = nil
				m.textInput.SetValue("")
				return m, nil
			}
		}

	case GotDef:
		m.loading = false

		if err := msg.Err; err != nil {
			m.err = err
			return m, nil
		}

		m.dicEntry = msg.DicEntry
		return m, nil
	}

	if m.typing {
		var cmd tea.Cmd
		m.textInput, cmd = m.textInput.Update(msg)
		return m, cmd
	}

	if m.loading {
		var cmd tea.Cmd
		m.spinner, cmd = m.spinner.Update(msg)
		return m, cmd
	}

	return m, nil
}

func (m Model) View() string {
	if m.typing {
		return fmt.Sprintf("Enter word:\n%s", m.textInput.View())
	}

	if m.loading {
		return fmt.Sprintf("Fetching definition %s", m.spinner.View())
	}

	if err := m.err; err != nil {
		return fmt.Sprintf("%v\n\nPress <Esc> to search another word", err)
	}

	return fmt.Sprintf("%s\nPress <Esc> to search another word",
		formatDicEntry(m.dicEntry))
}

func formatDicEntry(de DicEntry) string {
	// lipgloss styles
	bold := lipgloss.NewStyle().Bold(true)
	italics := lipgloss.NewStyle().Italic(true)

	data := de[0] // idk why the api sends this data as an array, there's only ever 1 item in it
	header := fmt.Sprintf(bold.Render(data.Word) + " " + italics.Render(data.Phonetics[0].Text) + "\n")
	body := ""
	for _, meaning := range data.Meanings {
		body += fmt.Sprintf(italics.Render(meaning.PartOfSpeech) + " " + meaning.Definitions[0].Definition + "\n")
	}

	return header + body
}
