
# **EModule**

## **목차**
- 시작하기
- `Module` & `start`
- `Write` & `Clear`
- `ReadSensor`
- `Logic`
- `register` & `unregister`
- `random`
- `flicker`
- `bzplay`
- `rainbow`

---

## 시작하기
> EModule 사용하여 PyC Basic II 장비를 제어하기 위해서는 `pop` 라이브러리가 필요합니다!

1. 새로운 Python 파일을 생성합니다.

2. 생성한 Python 파일에 다음과 같은 내용을 추가합니다.
```python

from EModule import Module, start

```

3. 자신이 필요한 추가 클래스 및 함수가 있다면, 이어서 추가합니다.
```python

from EModule import Write, Clear
from EModule import ReadSensor
from EModule import Logic
from EModule import register, unregister
from EModule import random
from EModule import flicker
from EModule import bzplay
from EModule import rainbow

```

4. 필요한 클래스를 사용하기위해 정의합니다.
```python

module = Module()
write = Write()
clear = Clear()
sensor = ReadSensor()
logic = Logic()

```

5. 프로그램의 시작점을 만든 후 아래와 같이 작성합니다.
```python

def main():
                            # 이 곳에 프로그램을 구현합니다.
    return module.wait()    # 프로그램의 대기를 위하여 호출합니다.


start(__name__, main)       # 시작점을 호출하여 프로그램을 실행합니다.
module.init()               # 입/출력을 초기화하기 위하여 호출합니다.

```

6. 터미널에 해당 커맨드를 입력하여 테스트 실행을 해봅니다.
```sh
python3 <파일_이름>.py
```

---

## `Module` & `start`
`Module`과 `start`는 EModule을 사용하기 위해 필수적으로 사용해야하는 클래스와 함수입니다.

### `Module` 클래스
Module 클래스는 프로그램의 초기화 및 대기 기능을 구현합니다.

|함수|기능|
|----|---|
|`init`|하드웨어의 모든 입/출력을 초기화합니다.|
|`wait`|사용자 입력 전까지 프로그램이 종료되지 않습니다.|


### `start` 함수
start 함수는 프로그램의 시작점을 정의합니다.
이는 직접 프로그램을 호출하였을 때만 시작점을 호출하고 이 이외에는 무시됩니다.
```python
start(__name__, <시작점_함수>)
```

---

## `Write` & `Clear`
`Write` & `Clear`는 하드웨어의 출력을 제어하기 위해 사용하는 클래스입니다.

### `Write` 클래스
Write 클래스는 하드웨어에 피드백이 발생합니다.

|함수|기능|매개변수|기본값|
|----|---|---|---|
|`pixel`|PixelDisplay에 글씨를 보여줍니다.|`표시_글씨`, `표시_간격`, `색상_값`|`[필수]`, `0.5`, `[255, 255, 255]`|
|`pixelfill`|PixelDisplay에 하나의 색상으로 채웁니다.|`색상_값`|`[255, 255, 255]`|
|`drawPixel`|PixelDisplay에 설정한 좌표에 색상을 표시합니다.|`x좌표`, `y좌표`, `색상_값`|`[필수]`, `[필수]`, `[255, 255, 255]`|
|`display`|OLED에 글씨를 작성합니다.|`표시_글씨`, `커스텀_위치`, `위치_값`|`[필수]`, `False`, `[0, 0]`|
|`ThreadDisplay`|OLED를 Callback으로 설정합니다.|-|-|
|`screen`|Callback한 OLED의 글씨를 변경합니다.|`표시_글씨`|`[필수]`|

* **pixel 예시**
```python

# PixelDisplay에 0.5초 간격으로 HelloWorld의 글자가 하얀색으로 표시됩니다.
write.pixel("HelloWorld")

# 1초 간격으로 초록색으로 보여주고 싶다면, 아래와 같이 파라미터를 수정합니다.
write.pixel("HelloWorld", 1.0, (0, 255, 0))

```

* **pixelfill 예시**
```python

# PixelDisplay에 꽉찬 하얀색으로 보여주고 싶다면, 이렇게 작성합니다.
write.pixelfill()

# 초록색으로 보여주고 싶다면, 아래와 같이 파라미터를 추가합니다.
write.pixel((0, 255, 0))

```

* **drawPixel 예시**
```python

# PixelDisplay의 8, 8 위치에 하얀색을 표시하고 싶다면, 이렇게 작성합니다.
write.drawpixel(8, 8)

# 색을 초록색으로 변경하고 싶다면, 마찬가지로 색상 파라미터를 추가합니다.
write.drawpixel(8, 8, (0, 255, 0))

# y8 좌표의 가로 Pixel을 모두 켜고 싶다면, 이렇게 작성합니다.
for x in range(16):
    write.drawpixel(x, 8)

```

* **display 예시**
```python

# Oled Display에 Hello, World!를 출력하고 싶다면, 이렇게 작성합니다.
write.display("Hello, World!")

# 줄바꿈하여 출력하고 싶다면, 문자열 리터널을 사용합니다.
write.display("Hello,\nWorld!")

# display를 뒷 내용을 이어서 계속해서 작성합니다. 커서를 처음으로 되돌리고 싶다면, 이렇게 작성합니다.
write.display("", True)

# 특정 위치에 글씨를 작성하고 싶다면, 파라미터에 좌표를 작성합니다.
write.display("Hello, World!", True, [24, 12])

```

* **ThreadDisplay와 screen 예시**
```python

# ThreadDisplay는 코드 지연을 방지하기 위해 사용합니다. 사용하기 위해서는 이렇게 작성합니다.
write.ThreadDisplay()

# ThreadDisplay를 활성화하였다면, display 함수 대신, screen 함수로 글씨를 바꿉니다.
write.screen("Hello, World!")

```

### `Clear` 클래스
Clear 클래스는 발생한 피드백 요소를 제거합니다.

|함수|기능|매개변수|
|----|---|---|
|`pixel`|PixelDisplay의 모든 요소를 제거합니다.|-|
|`display`|OLED의 모든 요소를 제거합니다.|-|

* **pixel 예시**
```python

# 모든 PixelDisplay 내용을 지우고 싶다면, 이렇게 작성합니다.
clear.pixel()

```

* **display 예시**
```python

# Oled Display 내용을 지우고 싶다면, 이렇게 작성합니다.
clear.display()

```

---

## `ReadSensor`
ReadSensor 클래스는 하드웨어의 입력 값을 반환합니다.
