접근


LV2

바이러스

출력 값은 K * (P^N) % (10^10 + 7) 으로 매우 간단한 식으로 표현 가능

문제는 K, P, N의 최대 값이 10^8 로 범위가 매우 크다 분모에 해당되는 부분을 자료형에 담기 어려움

int가 4바이트 자료형일때 unsigned로 최대 2^32 - 1 까지 가능 대략 10^9

P가 0이 아닐 때, A를 P로 나눈 나머지는 R 이다. 여기서 
A = B * P + R 일때 양변에 X를 곱하면
A * X = (B * X) * P + R * X 가 되고 이때 나머지는 (R * X) % P

즉 A에 계속해서 X를 곱하는 연산을 할 때 나머지 값은 이전 연산의 나머지에 X를 곱한 값의 나머지가 된다. 

여기서 A에 해당되는 K 값은 최대가 10^8로 P에 해당하는 10^10 + 7 보다 클 수 없다.

