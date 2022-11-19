package main

import (
	"errors"
	"fmt"
	"os"

	tea "github.com/charmbracelet/bubbletea"
)

func main() {
	err := tea.NewProgram(initialModel(), tea.WithAltScreen()).Start()
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
}

func initialModel() Model {
	initialBoard := Board{
		{" ", " ", " ", " ", " ", " ", " "},
		{" ", " ", " ", " ", " ", " ", " "},
		{" ", " ", " ", " ", " ", " ", " "},
		{" ", " ", " ", " ", " ", " ", " "},
		{" ", " ", " ", " ", " ", " ", " "},
		{" ", " ", " ", " ", " ", " ", " "},
	}

	return Model{
		board:     initialBoard,
		cursorPos: 0,
		turn:      "Y",
		win:       false,
	}
}

type Model struct {
	board     Board
	cursorPos int
	turn      string
	win       bool
}

type Board [6][7]string

func (m Model) Init() tea.Cmd {
	return nil
}

func (m Model) Update(msg tea.Msg) (tea.Model, tea.Cmd) {
	switch msg := msg.(type) {
	case tea.KeyMsg:
		if m.win {
			switch msg.String() {
			case "esc":
				//start new game
				newModel := initialModel()
				newModel.cursorPos = m.cursorPos
				return newModel, nil
			case "ctrl+c":
				return m, tea.Quit
			default:
				return m, nil
			}
		}

		switch msg.String() {
		// supports arrow keys, WASD, HJKL
		case "left", "h", "a":
			if m.cursorPos > 0 {
				m.cursorPos -= 1
				return m, nil
			}
		case "right", "l", "d":
			if m.cursorPos < 6 {
				m.cursorPos += 1
				return m, nil
			}
		case "enter", " ":
			newBoard, err := placePiece(m.board, m.turn, m.cursorPos)
			if err != nil {
				return m, nil
			}
			m.board = newBoard

			m.win = checkWin(m.board, m.cursorPos)

			if !m.win {
				// next player's turn
				if m.turn == "Y" {
					m.turn = "R"
				} else {
					m.turn = "Y"
				}
			}

			return m, nil
		case "ctrl+c":
			return m, tea.Quit
		}
	}
	return m, nil
}

func checkWin(b Board, cursorPos int) bool {
	win := false
	for _, row := range b {
		if checkRowWin(row) == true {
			win = true
		}
	}

	if checkColWin(b, cursorPos) == true {
		win = true
	}

	if checkDiagonalWin(b) == true {
		win = true
	}

	return win
}

func checkRowWin(row [7]string) bool {
	win := false
	for i := 0; i < len(row)-3; i++ {
		if row[i] != " " &&
			row[i] == row[i+1] &&
			row[i+1] == row[i+2] &&
			row[i+2] == row[i+3] {
			win = true
		}
	}

	return win
}

func checkColWin(b Board, col int) bool {
	// Count how many cols in a row match
	matchCounter := 0
	prevColSquare := " "
	for i := 0; i < len(b[0]); i++ {
		for _, row := range b {
			// check counter before so if there is a match it doesn't reset to 0
			if matchCounter >= 3 {
				return true
			}

			if row[col] != " " &&
				row[col] == prevColSquare {
				matchCounter += 1
			} else {
				matchCounter = 0
			}
			prevColSquare = row[col]
		}

		// for last row last column
		if matchCounter >= 3 {
			return true
		}

		// reset to check next col
		prevColSquare = " "
	}

	return false
}

func checkDiagonalWin(b Board) bool {
	win := false
	// check downwards diagonals
	for col := 0; col < len(b[0])-3; col++ {
		for row := 0; row < len(b)-3; row++ {
			if b[row][col] != " " &&
				b[row][col] == b[row+1][col+1] &&
				b[row+1][col+1] == b[row+2][col+2] &&
				b[row+2][col+2] == b[row+3][col+3] {
				win = true
			}
		}
	}

	// check upwards diagonals
	for col := 0; col < len(b[0])-3; col++ {
		for row := len(b) - 1; row > 2; row-- { // 2 to skip first 2 rows
			if b[row][col] != " " &&
				b[row][col] == b[row-1][col+1] &&
				b[row-1][col+1] == b[row-2][col+2] &&
				b[row-2][col+2] == b[row-3][col+3] {
				win = true
			}
		}
	}

	return win
}

func placePiece(b Board, piece string, col int) (Board, error) {
	for row := 5; row >= 0; row-- {
		if b[row][col] == " " {
			b[row][col] = piece
			return b, nil
		}
	}

	return b, errors.New("Column full")
}

func (m Model) View() string {
	display := ""
	if !m.win {
		display += renderCursor(m.cursorPos, m.turn)
	} else {
		display += fmt.Sprintf("%s wins! Press <Esc> to play again\n", m.turn)
	}
	display += renderBoard(m.board)
	return display
}

func renderBoard(b Board) string {
	bString := ""
	for _, row := range b {
		rowString := "|"
		for _, tile := range row {
			rowString += tile + "|"
		}
		bString += rowString + "\n"
	}
	return bString
}

func renderCursor(cursorPos int, piece string) string {
	allPos := []string{" ", " ", " ", " ", " ", " ", " "}
	allPos[cursorPos] = piece
	cursorLine := " "
	for _, pos := range allPos {
		cursorLine += pos + " "
	}
	return cursorLine + "\n"
}
