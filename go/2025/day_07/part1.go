package main

import (
	"aoc/utils"
	"fmt"
	"slices"
)

const FILENAME = "input.txt"

func getStart(board utils.Board) utils.P {
	for pos, value := range board {
		if value == "S" {
			return pos
		}
	}
	return utils.P{0, 0}
}

// Move beam downward
func moveBeam(beam utils.P, board utils.Board) []utils.P {
	nextPos := utils.P{beam[0] + 1, beam[1]}
	if board[nextPos] == "^" {
		// return two-element slice with utils.P{beam[0] + 1, beam[1] - 1} and utils.P{beam[0] + 1, beam[1] + 1}
		// We will assume we don't go out of bounds -- checked the inputs.
		return []utils.P{{beam[0] + 1, beam[1] - 1}, {beam[0] + 1, beam[1] + 1}}

	}

	// Just return single item slice with just nextPos
	return []utils.P{nextPos}
}

// Move all the beams to next iteration. Returns tuple of new beams and num splits.
func moveAllBeams(beams []utils.P, board utils.Board) ([]utils.P, int) {
	allNewBeams := []utils.P{}
	numSplits := 0
	for _, beam := range beams {
		newBeams := moveBeam(beam, board)

		// There is a split if we return 2.
		if len(newBeams) == 2 {
			numSplits++
		}

		// Add the positions we didn't have in newBeams.
		for _, newBeam := range newBeams {
			if !slices.Contains(allNewBeams, newBeam) {
				allNewBeams = append(allNewBeams, newBeam)
			}
		}

	}
	return allNewBeams, numSplits
}

func main() {
	lines := utils.ReadLines(FILENAME)
	board := utils.GetBoard(lines)
	sPos := getStart(board)
	fmt.Printf("Start: %v\n", sPos)
	fmt.Printf("Number of rows: %v\n", len(lines))

	// Track active beam locations.
	beams := []utils.P{}
	beams = append(beams, utils.P{sPos[0] + 1, sPos[1]})

	tot := 0
	for {
		newBeams, numSplits := moveAllBeams(beams, board)
		// fmt.Printf("New beams: %v\n", newBeams)
		// fmt.Printf("Num splits: %v\n", numSplits)
		tot += numSplits

		// If we have reached the bottom, break.
		if newBeams[0][0] == len(lines)-1 {
			break
		}

		beams = newBeams
	}

	fmt.Println("Part 1: ", tot)
}
