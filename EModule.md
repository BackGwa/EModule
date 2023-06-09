
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

|함수|기능|매개변수|
|----|---|---|
|`init`|하드웨어의 모든 입/출력을 초기화합니다.|-|
|`wait`|사용자 입력 전까지 프로그램이 종료되지 않습니다.|-|


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

|함수|기능|매개변수|
|----|---|---|
|`pixel`|PixelDisplay에 글씨를 보여줍니다.|`표시_글씨`, `표시_간격`, `색상_값`|
|`pixelfill`|PixelDisplay에 하나의 색상으로 채웁니다.|`색상_값`|
|`drawPixel`|PixelDisplay에 설정한 좌표에 색상을 표시합니다.|`x좌표`, `y좌표`, `색상_값`|
|`display`|OLED에 글씨를 작성합니다.|`표시_글씨`|
|`ThreadDisplay`|OLED를 Callback으로 설정합니다.|-|
|`screen`|Callback한 OLED의 글씨를 변경합니다.|`표시_글씨`|

### `Clear` 클래스
Clear 클래스는 발생한 피드백 요소를 제거합니다.

|함수|기능|매개변수|
|----|---|---|
|`pixel`|PixelDisplay의 모든 요소를 제거합니다.|-|
|`display`|OLED의 모든 요소를 제거합니다.|-|

---

## `ReadSensor`
ReadSensor 클래스는 하드웨어의 입력 값을 반환합니다.
