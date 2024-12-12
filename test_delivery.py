import pytest

# Расчет доставки
def cost_of_delivery(dist:float, dim:str, frag:bool, workload:float):
    delivery = 0

    if (frag == True) and (dist > 30):
        return "Хрупкие грузы нельзя возить на расстояние более 30 км"
    elif frag == True:
        delivery = delivery + 300

    if dist > 30:
        delivery = delivery+300
    elif 10 < dist <= 30:
        delivery = delivery + 200
    elif 2 < dist <= 10:
        delivery = delivery + 100
    else:
        delivery = delivery + 50

    if dim == "big":
        delivery = delivery + 200
    else:
        delivery = delivery + 100

    if workload == 3:
        delivery = delivery*1.6
    elif workload == 2:
        delivery = delivery*1.4
    elif workload == 1:
        delivery = delivery * 1.2
    else:
        delivery = delivery

    if delivery < 400:
        delivery = 400

    return delivery

# Тестовые наборы данных (dist:float, dim:str, frag:bool, workload:float, result)
data  = [
    (31, "big", True, 0, "Хрупкие грузы нельзя возить на расстояние более 30 км"),
    (31, "small", False, 1, 480),
    (30, "small", True, 0, 600),
    (10, "big", False, 2, 420),
    (2, "big", True, 3, 880),
    (0, "small", False, 0, 400)
]

# Тестовая функция
@pytest.mark.parametrize("dist, dim, frag, workload, exp_result", data)
def test_delivery(dist, dim, frag, workload, exp_result):
    result = cost_of_delivery(dist, dim, frag, workload)
    assert result==exp_result, f"Cтоимость доставки не соответствует ожидаемой, ожидается {exp_result}"

