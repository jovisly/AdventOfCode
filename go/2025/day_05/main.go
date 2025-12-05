package main

import (
	"aoc/utils"
	"fmt"
	"sort"
	"strconv"
	"strings"
)

const FILENAME = "input.txt"

type Range struct {
	Min int
	Max int
}

func mergeRanges(rangeStrings []string) []Range {
	ranges := make([]Range, 0)
	for _, r := range rangeStrings {
		if len(r) == 0 {
			continue
		}
		parts := strings.Split(r, "-")
		min, err := strconv.Atoi(parts[0])
		if err != nil {
			panic(err)
		}
		max, err := strconv.Atoi(parts[1])
		if err != nil {
			panic(err)
		}
		ranges = append(ranges, Range{Min: min, Max: max})
	}

	// Sort by min. Iteratively go through pairs of ranges. Merge as needed.
	sort.Slice(ranges, func(i, j int) bool {
		return ranges[i].Min < ranges[j].Min
	})

	if len(ranges) == 0 {
		return []Range{}
	}

	merged := []Range{ranges[0]}
	for i := 1; i < len(ranges); i++ {
		current := ranges[i]
		lastIdx := len(merged) - 1

		if current.Min <= merged[lastIdx].Max {
			if current.Max > merged[lastIdx].Max {
				merged[lastIdx].Max = current.Max
			}
		} else {
			merged = append(merged, current)
		}
	}

	return merged
}

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

	fmt.Println("Part 1: ", num)

	// Merge overlapping ranges
	merged := mergeRanges(ranges)
	// fmt.Println("Merged ranges:")
	// for _, r := range merged {
	// 	fmt.Printf("  %d-%d\n", r.Min, r.Max)
	// }
	num2 := 0
	for _, m := range merged {
		num2 += m.Max - m.Min + 1
	}

	fmt.Println("Part 2: ", num2)
}
