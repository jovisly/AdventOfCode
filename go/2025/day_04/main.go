package main

import (
	"aoc/utils"
	"fmt"
)

const FILENAME = "input.txt"

func processBoard1(board utils.Board) int {
	num := 0
	// Go through every position on the board.
	for pos, value := range board {
		if value != "@" {
			continue
		}

		neighborValues := utils.GetNeighborValues8(board, pos)
		numNeighbors := 0
		for _, neighborValue := range neighborValues {
			if neighborValue == "@" {
				numNeighbors++
			}
		}
		if numNeighbors < 4 {
			num++
		}

	}

	return num
}

func oneIteration(board utils.Board) utils.Board {
	// Maybe we will just mutate the board in place? Is that an okay thing to do in Go?
	for pos, value := range board {
		if value != "@" {
			continue
		}

		neighborValues := utils.GetNeighborValues8(board, pos)
		numNeighbors := 0
		for _, neighborValue := range neighborValues {
			if neighborValue == "@" {
				numNeighbors++
			}
		}
		if numNeighbors < 4 {
			board[pos] = "."
		}
	}

	return board
}

func countRolls(board utils.Board) int {
	num := 0
	for _, value := range board {
		if value == "@" {
			num++
		}
	}
	return num
}

func main() {
	lines := utils.ReadLines(FILENAME)
	board := utils.GetBoard(lines)
	fmt.Println("Part 1: ", processBoard1(board))

	numRemoved := 0
	totalNumRemoved := 0

	for {
		prevNum := countRolls(board)
		board = oneIteration(board)
		currNum := countRolls(board)
		numRemoved = prevNum - currNum

		if numRemoved == 0 {
			break
		}
		totalNumRemoved += numRemoved
	}

	fmt.Println("Part 2: ", totalNumRemoved)
}
