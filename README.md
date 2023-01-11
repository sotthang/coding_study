# 코딩테스트 연습
1일 최소 1문제 풀기를 지향하며 프로그래머스, 백준 사이트에서 진행합니다
<br>
더 좋은 풀이의 PR 은 언제나 환영입니다
<br>
<br>

## 백준 문제 입력 받는 방법
입력 값이 integer 하나인 경우

```python
a = int(input())
```
or
```python
import sys

a = int(sys.stdin.readline())
```
<br>

입력 값이 string 하나인 경우

```python
a = str(input())
```
or
```python
import sys

a = str(sys.stdin.readline().strip())
```
<br>

입력 값이 integer 2개인 경우

```python
x, y = map(int, input().split())
```
or
```python
import sys

x, y = map(int, sys.stdin.readline().split())
```
<br>

입력 값이 integer 여러 개인 경우 (리스트에 하나씩)

```python
x = list(map(int, input().split()))
```
or
```python
import sys

x = list(map(int, sys.stdin.readline().split()))
```

input 과 sys.stdin.readline() 은 입력 속도의 차이가 크기에 
<br>
sys.stdin.readline() 코드를 사용하면 시간 초과로 인한 에러를 줄일 수 있다
<br>
혹은 아래 코드를 사용하면 input 이 sys.stdin.readline 의 속도를 가지게 되기에 input 을 사용해도 된다
<br>
(내장함수 input 대신 sys.stdin.readline 코드를 사용하는 input 이 됨)

```python
import sys

input = sys.stdin.readline
```
<br>
[입력 속도 비교](https://www.acmicpc.net/blog/view/56)
<br>
<br>
input() 과 sys.stdin.readline() 의 차이
<br>
input() 은 parameter로 prompt message를 받을 수 있지만, sys.stdin.readline()은 prompt message를 인수로 받지 않음
<br>
input() 은 입력받은 값의 개행 문자를 삭제시켜서 리턴하지만, sys.stdin.readline()은 개행 문자를 포함한 값을 리턴
