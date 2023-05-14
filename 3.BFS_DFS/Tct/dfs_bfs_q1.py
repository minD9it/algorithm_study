'''
1. "균형 잡힌 괄호 문자열" 분할하는 함수
2. "올바른 괄호 문자열"인지 확인하는 함수
3. 최종 재귀함수
'''

# 1. "균형 잡힌 괄호 문자열" 분할 함수
# parms: 괄호 문자열
# return 균형잡힌 괄호 문자열을 분할할 위치 인덱스
def balanced(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return i
        

# 2. "올바른 괄호 문자열" 확인 함수
def check(p):
    cnt = 0
    for i in p:
        if i == '(':
            cnt += 1
        else: 
            if cnt == 0: # '('로 시작하지 않는 괄호 문자열이라는 소리임으로 올바른 괄호 문자열이 아님
                return False
            cnt -= 1
    return True         

def solution(p):
    answer = ''
    # 알고리즘 1. 빈 문자열이면 그냥 반환
    if p == '':
        return answer
    # 알고리즘 2. 분할
    index = balanced(p)
    u = p[:index + 1]
    v = p[index + 1:]
    # 알고리즘 3. 분할된 u 문자열이 올바른 문자열인지 확인
    if check(u): # 3-1. 올바른 문자열인 경우
        answer = u + solution(v) # 분할 문자열 v에 대해서는 다시 처음부터 진행
    else: # 알고리즘 4. 분할된 u 문자열이 올바른 문자열이 아닌 경우
        answer = '('
        answer += solution(v)
        answer += ')'
        u = u[1:-1]
        for i in u:
            if i == '(':
                answer += ')'
            else:
                answer += '('

    return answer

