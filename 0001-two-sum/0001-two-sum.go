func twoSum(nums []int, target int) []int {
    hashMap := make(map[int]int)
    for i, v := range nums {
        diff := target - v
        val, exists := hashMap[diff]
        if exists {
            return []int{i, val}
        }
        hashMap[v] = i
    }
    return []int{-1,-1}
}