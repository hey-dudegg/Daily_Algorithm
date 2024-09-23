"""
2차원 리스트(행렬) 더하기!
arr1, arr2

[
    [1, 2],
    [2, 3]
]
"""
def solution(arr1, arr2):
    row = len(arr1)
    col = len(arr1[0])
    
    answer = []
    
    for i in range(row):
        tmp_row = []
        
        for j in range(col):
            tmp_row.append(arr1[i][j] + arr2[i][j])
        
        answer.append(tmp_row)
    
    return answer