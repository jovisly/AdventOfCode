package main

import (
	"aoc/utils"
	"fmt"
	"slices"
	"strconv"
	"strings"
)

const FILENAME = "input.txt"


func processRanges(ranges []string) []int {
	ingredients := []int{}
	for _, r := range ranges {
		parts := strings.Split(r, "-")
		min, err := strconv.Atoi(parts[0])
		if err != nil {
			panic(err)
		}
		max, err := strconv.Atoi(parts[1])
		if err != nil {
			panic(err)
		}
		for i := min; i <= max; i++ {
			if !slices.Contains(ingredients, i) {
				ingredients = append(ingredients, i)
			}
		}
	}
	return ingredients
}


func main() {
	content := utils.ReadFile(FILENAME)
	parts := strings.Split(content, "\n\n")
	ranges := strings.Split(parts[0], "\n")
	ingredients := strings.Split(parts[1], "\n")

	freshIngredients := processRanges(ranges)
	num := 0
	for ingredient := range ingredients {
		if slices.Contains(freshIngredients, ingredient) {
			num += 1
		}
	}

	// IMPLEMENT
	fmt.Println("Part 1: ", num)
	fmt.Println("Part 2: ")
}
