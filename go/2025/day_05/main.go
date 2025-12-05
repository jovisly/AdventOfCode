package main

import (
	"aoc/utils"
	"fmt"
	"strconv"
	"strings"
)

const FILENAME = "input.txt"


func isFresh(ingredient string, ranges []string) bool {
	if len(ingredient) == 0 {
		return false
	}
    intIngredient, err := strconv.Atoi(ingredient)
    if err != nil {
        panic(err)
    }
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
        if intIngredient >= min && intIngredient <= max {
            return true
        }
    }
    return false
}


func main() {
	content := utils.ReadFile(FILENAME)
	parts := strings.Split(content, "\n\n")
	ranges := strings.Split(parts[0], "\n")
	ingredients := strings.Split(parts[1], "\n")

	num := 0
	for _, ingredient := range ingredients {
		// fmt.Println(ingredient)
		if isFresh(ingredient, ranges) {
			num += 1
		}
	}

	// IMPLEMENT
	fmt.Println("Part 1: ", num)
	fmt.Println("Part 2: ")
}
