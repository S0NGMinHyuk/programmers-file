def solution(number, k):
    # stack에 입력값을 순서대로 삽입 
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
        # 들어오는 값이 stack 값보다 크면, 기존의 값을 제거하고 새로운 값으로 바꿈 
            k -= 1 # 값을 한개 빼서 k는 1이 제거 
            stack.pop() # 내부의 값을 제거 

        stack.append(num)
        # 새로운 값을 삽입 
    if k != 0:
        stack = stack[:-k]
    # 만일 k 만큼 제거하지 못했으면 남은 부분은 뒤부터 삭제
    return ''.join(stack)