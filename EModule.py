# [IMPORT MODULE]
from pop import Leds, Oled, PiezoBuzzer, Pixels
from pop import Switches, Pir, Ultrasonic, Cds, Potentiometer, Psd, TempHumi, Sound, Apds
from time import sleep as delay
import random as rd


# [INPUT CLASS INIT]
sw = Switches()
pir = Pir()
sonic = Ultrasonic()
cds = Cds()
psd = Psd()
meter = Potentiometer()
temphumi = TempHumi()
sound = Sound()
color = Apds()

# [OUTPUT CLASS INIT]
led = Leds()
display = Oled()
bz = PiezoBuzzer()
dot = Pixels()


# [CLASS] : Module
class Module():
    
    # [FUNCTION] : init
    def init(self):
        """
        ## [FUNCTION] : init
        init 함수는 모든 상태를 초기상태로 변경합니다.
        """
        led.off()
        display.clearDisplay()
        dot.clear()
        return
    
    
    # [FUNCTION] : wait
    def wait(self):
        """
        ## [FUNCTION] : wait
        wait 함수는 Callback를 위하여 사용자의 입력을 대기합니다.
        """
        return input('[ ENTER를 눌러 다음 코드를 실행하거나 종료합니다. ]')
    


# [CLASS] : Write
class Write():
    
    # [FUNCTION] : pixel
    def pixel(self, text, time = 0.5, color = [255, 255, 255]):
        """
        ## [FUNCTION] : pixel
        입력한 파라미터를 기반으로 PixelDisplay에 글씨를 보여줍니다.
        """
        for i in text:
            dot.drawChar(i, color)
            delay(time)
            dot.clear()
        return
    
    
    # [FUNCTION] : display
    def display(self, text):
        """
        ## [FUNCTION] : display
        입력한 파라미터를 기반으로 OLED에 글씨를 보여줍니다.
        """
        return display.print(text)


# [CLASS] : ReadSensor
class ReadSensor():
    
    # [FUNCTION] : switch
    def switch(self, key = 0):
        """
        ## [FUNCTION] : switch
        현재 모든 스위치의 키 값을 반환하거나 파라미터를 기반으로 특정 키의 값을 bool 형식으로 반환합니다.
        """
        return (True if(sw.read(key) == 1) else False) if(key != 0) else sw.read()


    # [FUNCTION] : pir
    def pir(self):
        """
        ## [FUNCTION] : pir
        PIR의 감지여부에서 따라 bool 형식으로 반환합니다.
        """
        return pir.read()


    # [FUNCTION] : sonic
    def sonic(self):
        """
        ## [FUNCTION] : sonic
        ULTRA SONIC 센서의 거리를 int 형식으로 반환합니다.
        """
        return sonic.read()


    # [FUNCTION] : cds
    def cds(self):
        """
        ## [FUNCTION] : cds
        CDS 센서에서 측정한 빛을 int 형식으로 반환합니다.
        """
        return cds.getValue()


    # [FUNCTION] : meter
    def readmeter(self):
        """
        ## [FUNCTION] : meter
        다이얼의 값을 int 또는 float 형식으로 반환합니다.
        """
        return meter.getValue()


    # [FUNCTION] : sound
    def readsound(self):
        """
        ## [FUNCTION] : sound
        마이크의 소리 값을 int 형식으로 반환합니다.
        """
        return sound.getValue()


    # [FUNCTION] : readpsd
    def psd(self):
        """
        ## [FUNCTION] : psd
        PSD 센서의 값을 int 형식으로 반환합니다.
        """
        return psd.getValue()


    # [FUNCTION] : color
    def color(self, target):
        """
        ## [FUNCTION] : color
        파라미터를 기반으로 COLOR 센서의 값을 다양한 형식으로 반환합니다.
        """
        if(target == 'proximity'):
            return color.readProximity()
        elif(target == 'ambientlight'):
            return color.readAmbientLight()
        elif(target == 'color'):
            return color.readColor()
        elif(target == 'gesture'):
            return color.readGesture()
        return
    
    
# [CLASS] : Clear
class Clear():
    
    # [FUNCTION] : pixel
    def pixel(self):
        """
        ## [FUNCTION] : pixel
        PixelDisplay에 모든 내용을 지웁니다.
        """
        return dot.clear()
    
    
    # [FUNCTION] : display
    def display(self):
        """
        ## [FUNCTION] : display
        OLED에 모든 내용을 지웁니다.
        """
        return display.clear()
    

# [CLASS] : Logic
class Logic:
    
    # [FUNCTION] : gate
    def gate(self, syntax, valueA = 0, valueB = 0):
        """
        ## [FUNCTION] : gate
        gate 함수는 조건 게이트식을 계산하여 반환합니다.
        """
        if(syntax == 'and'):
            return 1 if(valueA == 1 and valueB == 1) else 0
        elif(syntax == 'or'):
            return 1 if(valueA == 1 or valueB == 1) else 0
        elif(syntax == 'not'):
            return 0 if(valueA == 1) else 1
        else:
            return 0


    # [FUNCTION] : ngate
    def ngate(self, syntax, valueA = 0, valueB = 0):
        """
        ## [FUNCTION] : ngate
        ngate 함수는 조건 게이트식을 계산하고 항시 부정하여 반환합니다.
        """
        if(syntax == 'and'):
            return self.gate('not', self.gate('and', valueA, valueB))
        elif(syntax == 'or'):
            return self.gate('not', self.gate('or', valueA, valueB))
        elif(syntax == 'not'):
            return self.gate('not', self.gate('not', valueA))
        else:
            return 0


# [FUNCTION] : register
def register(target, function):
    """
    ## [FUNCTION] : register
    register 함수는 특정 기능과 함수를 Callback 상태로 전환합니다.
    """
    if(target == 'switch'):
        sw.registerCallback(function)
    elif(target == 'pir'):
        pir.registerCallback(function)
    elif(target == 'sonic'):
        sonic.registerCallback(function)
    elif(target == 'temphumi'):
        temphumi.registerCallback(function)
    elif(target == 'apds'):
        color.registerCallback(function)
    return


# [FUNCTION] : unregister
def unregister(target):
    """
    ## [FUNCTION] : unregister
    unregister 함수는 특정 기능의 Callback 상태를 취소합니다.
    """
    if(target == 'switch'):
        sw.unregisterCallback()
    elif(target == 'pir'):
        pir.unregisterCallback()
    elif(target == 'sonic'):
        sonic.unregisterCallback()
    elif(target == 'temphumi'):
        temphumi.unregisterCallback(function)
    elif(target == 'apds'):
        color.unregisterCallback(function)
    return


# [FUNCTION] : random
def random(vartype, min = 0, max = 100):
    """
    ## [FUNCTION] : random
    random 함수는 파라미터를 기반으로 랜덤한 값을 반환합니다.
    """
    return rd.randint(min, max) if(vartype == 'int') else (rd.uniform(min, max) if(vartype == 'float') else 0)
    

# [FUNCTION] : flicker
def flicker(count = 1, time = 0.5, pin = 0):
    """
    ## [FUNCTION] : flicker
    flicker 함수는 입력한 파라미터를 기반으로 LED를 깜빡입니다.
    """
    for n in range(count):
        if(pin != 0):
            led.on(pin)
            delay(time)
            led.off(pin)
        else:
            led.on()
            delay(time)
            led.off()
        delay(time)
    return


# [FUNCTION] : bzplay
def bzplay(key, sound, time):
    """
    ## [FUNCTION] : bzplay
    입력한 파라미터를 기반으로 부저에서 소리를 발생시킵니다.
    """
    return bz.tone(key, sound, time)


# [FUNCTION] : rainbow
def rainbow(fps = 30, count = 2):
    """
    ## [FUNCTION] : rainbow
    파라미터를 기반으로 PixelDisplay에 무지개 효과를 재생합니다.
    """
    return dot.rainbow(fps, count)


# [FUNCTION] : start
def start(file, function):
    """
    ## [FUNCTION] : start
    프로그램의 시작점을 정의합니다.
    """ 
    if file == '__main__':
        return function()
    else:
        return -1