class Foo:
    def __init__(self):
        "yeni bir sınıf örneği oluşturulduğunda, bu örneğin _sayi özelliği 10 olarak atanır."
        self._sayi = 10


class Bar:
    def __init__(self, sayi=10):
        """
        bu sınıfı oluşturuken, sayıyı değiştirmenize izin verir. Öntanımlı değeri 10dur
        a = Bar()
        b = Bar(20)
        a._sayi => 10
        b._sayi => 20
        """
        self._sayi = sayi

bar1=Bar(sayi=22)

print(bar1._sayi)
