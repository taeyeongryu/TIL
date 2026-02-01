def mul(m):
    """
    외부 함수: m을 인자로 받아 내부 함수 wrapper를 반환합니다.
    """
    def wrapper(n):
        """
        내부 함수 (클로저): 외부 함수의 변수 m을 참조(캡처)합니다.
        """
        return m * n
    return wrapper

if __name__ == "__main__":
    # 1. 클로저 생성
    mul3 = mul(3)
    mul4 = mul(4)

    # 2. 클로저 호출 (상태가 유지됨을 확인)
    print(f"mul3(10): {mul3(10)}")  # 30 (3 * 10)
    print(f"mul4(10): {mul4(10)}")  # 40 (4 * 10)

    # 3. 실제 변수 확인 (__closure__)
    # mul3는 내부적으로 m=3 이라는 값을 배낭(Cell object)에 담고 있습니다.
    print("\n--- Closure Inspection ---")
    if mul3.__closure__:
        captured_value = mul3.__closure__[0].cell_contents
        print(f"mul3가 기억하고 있는 변수 m의 값: {captured_value}")
    
    # mul4는 다른 배낭에 m=4 를 담고 있습니다.
    if mul4.__closure__:
        captured_value = mul4.__closure__[0].cell_contents
        print(f"mul4가 기억하고 있는 변수 m의 값: {captured_value}")

