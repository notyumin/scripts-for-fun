import System.IO

main :: IO ()
main = do
  hSetBuffering stdin NoBuffering
  hSetBuffering stdout NoBuffering
  putStr "Weight (kg): "
  w <- getDoubleInput
  putStr "Height (m): "
  h <- getDoubleInput
  print (calcBmi h w)

calcBmi :: Double -> Double -> Double
calcBmi height weight = weight / (height ^ 2)

getDoubleInput :: IO Double
getDoubleInput = do
  inputStr <- getLine
  let d = read inputStr :: Double
  return d
