**Практическая часть №4**

**Задание 1. Базовая структура (Умный дом)**

Спроектируйте класс SmartLight (Умная лампочка).

Прибор должен иметь следующие характеристики:  
**Атрибуты:**

- brightness (яркость, целое число) — доступно всем.
- color (цвет, строка) — доступно всем.
- is_on (включена ли, булево) — скрытое (приватное) свойство, чтобы нельзя было включить "в обход" выключателя.

**Методы:**

- turn_on() — включить.
- turn_off() — выключить.
- set_color(new_color) — изменить цвет.

![](file:///C:/Users/gasil/AppData/Local/Temp/msohtmlclip1/01/clip_image002.jpg)  
[https://mermaid.live/edit#pako:eNplkEtvhCAUhf8KuSsntRN8jYVtu-yuu8ZkwiiiicIELunD-N-LOm1telnA_c65h8AEtWkkcKgH4dxTL5QVY6VJqJWQl1FYfO5Vh2Ta-FJ3vUZysQvW0rmd4ND2WpHaDMb-4vuLMQPp3dnonRe91YFEh3-sbf9AJ_G8Jka3eC3fNrB3qeByKNC76EA246bOywYxKNs3wNF6GcMo7SiWFtZnVYCdHGUFPBwb2Qo_YAWVnsPYVehXY8bvSWu86oC3YnCh89dGoLx93I9F6kbaR-M1Ai_WBOATvAPPWHI80eyUJWlJwwriB3CWBZizjOVBoqxkcwyf65X0WBY0f0iLgqU0T2hymr8AguCDHg](https://mermaid.live/edit#pako:eNplkEtvhCAUhf8KuSsntRN8jYVtu-yuu8ZkwiiiicIELunD-N-LOm1telnA_c65h8AEtWkkcKgH4dxTL5QVY6VJqJWQl1FYfO5Vh2Ta-FJ3vUZysQvW0rmd4ND2WpHaDMb-4vuLMQPp3dnonRe91YFEh3-sbf9AJ_G8Jka3eC3fNrB3qeByKNC76EA246bOywYxKNs3wNF6GcMo7SiWFtZnVYCdHGUFPBwb2Qo_YAWVnsPYVehXY8bvSWu86oC3YnCh89dGoLx93I9F6kbaR-M1Ai_WBOATvAPPWHI80eyUJWlJwwriB3CWBZizjOVBoqxkcwyf65X0WBY0f0iLgqU0T2hymr8AguCDHg)

**Задание 2. Инкапсуляция и Безопасность (Банковская карта)**

Спроектируйте класс CreditCard.

Банковская сфера требует защиты данных, поэтому:

- Номер карты (number) и CVC-код (cvc) должны быть **приватными** (-).
- Имя владельца (owner_name) может быть **публичным** (+).
- Баланс (balance) должен быть **защищенным** (#) (доступен классу и его наследникам, но не всем подряд).

Добавьте методы:

- pay(amount) — публичный метод оплаты.
- check_pin(pin) — приватный метод проверки пин-кода (вызывается внутри метода оплаты).

![](file:///C:/Users/gasil/AppData/Local/Temp/msohtmlclip1/01/clip_image004.jpg)

[https://mermaid.live/edit#pako:eNqFU91u2jAUfhXL3IQSUCBASG7ZU0yRkEkMRE1sZJxtHUJau4up2qRpV7vsK7RV0ZAm2CvYb7TjhCasVFp-7e-c833nJ1njiMcUBzhKyWr1JiFzQbKQITgKBI0FjRM5JiJG6xI3R3slRcLmiOXZlIpzPHoXnYPLhNVgY5ZyItGUpIRFtMZbR2f-nlExYSQ7tdXJWHUCNqpFJ6aaCig4qh3IH82ldMISOTnqN09EluTKKj1IxnMmK4KELXM5AZommnKenhQYLWh0aSzW_1xbc1qJWs2LMpUX5oysLmk8KXtrnErS0mtTvhiXFM24OJ1PiNWd_qR26lHd6xu111_VFqk_6qB-6-_IajeDMGTt55mZpRmTeZvJhOZSPyH0Vu30rf6h9nAeKgpYWI2ColFNrYy505_VAzjs9JeziFYR0TodZxF0gf5pBFI79Erphv0JqB7UPRQFhKYoBJApCFQLm76GYqFk23iDPoLHFukbaMUWIg_GVmR3rb8h9YjUL9g_wb2HVu1CbBqKbTwXSYwDKXJq44yKjJgtLr75EMsFhcxxAMuYzkieShO3gbAlYW85z54jBc_nCxzMSLqCXb6MiaTHv6pCBWUxFWPzbeHA7RUcOFjjDzjo95xO3-16brfv9nzHd1wbX-HA9zueN_D9wcjtDftOd7Sx8cdC1ekMvdFg2Bt5Pjxdz_M3fwFJCXxJ](https://mermaid.live/edit#pako:eNqFU91u2jAUfhXL3IQSUCBASG7ZU0yRkEkMRE1sZJxtHUJau4up2qRpV7vsK7RV0ZAm2CvYb7TjhCasVFp-7e-c833nJ1njiMcUBzhKyWr1JiFzQbKQITgKBI0FjRM5JiJG6xI3R3slRcLmiOXZlIpzPHoXnYPLhNVgY5ZyItGUpIRFtMZbR2f-nlExYSQ7tdXJWHUCNqpFJ6aaCig4qh3IH82ldMISOTnqN09EluTKKj1IxnMmK4KELXM5AZommnKenhQYLWh0aSzW_1xbc1qJWs2LMpUX5oysLmk8KXtrnErS0mtTvhiXFM24OJ1PiNWd_qR26lHd6xu111_VFqk_6qB-6-_IajeDMGTt55mZpRmTeZvJhOZSPyH0Vu30rf6h9nAeKgpYWI2ColFNrYy505_VAzjs9JeziFYR0TodZxF0gf5pBFI79Erphv0JqB7UPRQFhKYoBJApCFQLm76GYqFk23iDPoLHFukbaMUWIg_GVmR3rb8h9YjUL9g_wb2HVu1CbBqKbTwXSYwDKXJq44yKjJgtLr75EMsFhcxxAMuYzkieShO3gbAlYW85z54jBc_nCxzMSLqCXb6MiaTHv6pCBWUxFWPzbeHA7RUcOFjjDzjo95xO3-16brfv9nzHd1wbX-HA9zueN_D9wcjtDftOd7Sx8cdC1ekMvdFg2Bt5Pjxdz_M3fwFJCXxJ)

**Задание 3. Наследование (Иерархия RPG)**

В компьютерной игре есть разные типы персонажей:

1. Есть базовый класс Character (Персонаж). У него есть имя (name) и метод move() (идти).
2. Есть Archer (Лучник). Он является персонажем. У него есть дополнительный метод shoot() (стрелять).
3. Есть Knight (Рыцарь). Он является персонажем. У него есть дополнительный метод attack_sword() (бить мечом).

![](file:///C:/Users/gasil/AppData/Local/Temp/msohtmlclip1/01/clip_image006.jpg)  
[https://mermaid.live/edit#pako:eNp1UctOwzAQ_JVoT61Iq8ZxmtrigsqNP0CR0Cp2k4jGrhynPEoOwA9xoCfEP6R_1DR9EFDZ087sjMdrryDWQgKHeI5FcZ1hYjCPlNNUyzjTFA3GVhpntad3dVFYk6nEUZjLDnvS9naDfmeS66Xs9Z2lzsSerboZVyZO_wakWtv_HTcqS1L7y4HWYnx_VzxoI84Zfxa5fBkMjpncqb_rj81r_VWv68_Ne73evJ3VHxLP6cGFxGQCuDWldCGXJscdhPZ6EdhUNs8EvGmFnGE5txFEqmpsC1S3WudHp9FlkgKf4bxoULkQaOXhS06skUpIM9WlssApa88AvoLHBoX-0KM0JOGYjeko9Fx4Au4Rf8gCjzES0onHPMoqF57b1NFwTCaUMELCEQmoHwTVFuc5rRg](https://mermaid.live/edit#pako:eNp1UctOwzAQ_JVoT61Iq8ZxmtrigsqNP0CR0Cp2k4jGrhynPEoOwA9xoCfEP6R_1DR9EFDZ087sjMdrryDWQgKHeI5FcZ1hYjCPlNNUyzjTFA3GVhpntad3dVFYk6nEUZjLDnvS9naDfmeS66Xs9Z2lzsSerboZVyZO_wakWtv_HTcqS1L7y4HWYnx_VzxoI84Zfxa5fBkMjpncqb_rj81r_VWv68_Ne73evJ3VHxLP6cGFxGQCuDWldCGXJscdhPZ6EdhUNs8EvGmFnGE5txFEqmpsC1S3WudHp9FlkgKf4bxoULkQaOXhS06skUpIM9WlssApa88AvoLHBoX-0KM0JOGYjeko9Fx4Au4Rf8gCjzES0onHPMoqF57b1NFwTCaUMELCEQmoHwTVFuc5rRg)

**Задание 4. Типы связей (Музыкальный плеер)**

Спроектируйте систему из двух классов: Playlist (Плейлист) и Song (Песня):

- Класс Song имеет название (title) и длительность (duration).
- Класс Playlist имеет название (name) и список песен.

![](file:///C:/Users/gasil/AppData/Local/Temp/msohtmlclip1/01/clip_image008.jpg)

[https://mermaid.live/edit#pako:eNptkdFKwzAUhl-lnKsNt7FmWbvmVh9A8E4KIyxZF2iTkaTgHAX1wltfZTAnXvkM6RuZtm5UMVcnX3Lyf4fsYaUYBwKrnBpzI2imaZHKwK-WBHdKZsG-I826MlYLj6ywOe9hIW3ASk2tULKHM26XQq7VYBh0jd1Z1Y-4zekuF8b-FyNp0U9prxmvZHqQMrZs2KB1barhHwOrLM2XZz3v4m1_iVwU1HjcjUwCd3DH-smd3NEd6lf3Wb8Fg_rZfbl3d_L8w5MXHwQjyLRgQKwu-QgKrgvabKGdJgW74X4EIL5kfE3L3KaQysq3bam8V6o4d2pVZhsga5obvyu3jFr-8yEXqrlkXF-rUlogUdi-AWQPD0BwPJuEGMcojpIIT2N_uAMSotkkmYdJgmK8CJMQJ9UIHtvU6SRCC4wSNMNTFC8iNK--AbWRrJw](https://mermaid.live/edit#pako:eNptkdFKwzAUhl-lnKsNt7FmWbvmVh9A8E4KIyxZF2iTkaTgHAX1wltfZTAnXvkM6RuZtm5UMVcnX3Lyf4fsYaUYBwKrnBpzI2imaZHKwK-WBHdKZsG-I826MlYLj6ywOe9hIW3ASk2tULKHM26XQq7VYBh0jd1Z1Y-4zekuF8b-FyNp0U9prxmvZHqQMrZs2KB1barhHwOrLM2XZz3v4m1_iVwU1HjcjUwCd3DH-smd3NEd6lf3Wb8Fg_rZfbl3d_L8w5MXHwQjyLRgQKwu-QgKrgvabKGdJgW74X4EIL5kfE3L3KaQysq3bam8V6o4d2pVZhsga5obvyu3jFr-8yEXqrlkXF-rUlogUdi-AWQPD0BwPJuEGMcojpIIT2N_uAMSotkkmYdJgmK8CJMQJ9UIHtvU6SRCC4wSNMNTFC8iNK--AbWRrJw)

**Задание 5. Комплексная система (Служба доставки)**

Проанализируйте текст и спроектируйте полную схему классов.

В системе есть **Заказ**. Каждый заказ обязательно состоит из нескольких **Товаров**. Товар не может существовать в контексте заказа без самого заказа, но у товара есть название и цена.  
У заказа есть статус.

Существуют разные виды доставки: **Курьер** и **Дрон**. И Курьер, и Дрон являются **Доставщиками**. У любого Доставщика есть скорость, но только Дрон умеет летать, а Курьер умеет звонить клиенту.

Заказ закрепляется за одним конкретным Доставщиком

**Алгоритм действий:**

1. Выделите 5 классов.
2. Определите, где Наследование (<|--).
3. Определите, где Композиция (*--).
4. Определите, где Агрегация (o--).

![](file:///C:/Users/gasil/AppData/Local/Temp/msohtmlclip1/01/clip_image010.jpg)

[https://mermaid.live/edit#pako:eNp9kt9O2zAUxl8lOleFlahJ06axKm7gfrueIiETnxZLjl3ZDhrrKm03u92ukXgHxB-BxAavYN4IN21pYNEsxbI_n9_5zjnKHArFEAgUghpzyOlU0zKXgV-1EnzSilWFDeYrcbk-GKu5nAaWW4ENeSIUtcFM82KtLpqJPmqGui2NsdRWpqELbpZpat-mbtAeMRT8FDXqzuHmFLCdFrvtc8NyPKbH3pUWdn__n8LNDJE11LVVZ1W4ajM5UJXm77oqqBBHheAobae1MK0kviEm4uxd5Mpyd2_vdfwkcOfu0f1xT36_c_fPP_33K-hEYbi704SUh7a9e-y3u37-7m7dtbtsQNEa2oaOv3ly05DnLnz8D_fgyRtveeUu3V93725bsVVP_4NyCV2Yas6AWF1hF0rUJV1eoR5FDvYES8yB-CPDCa2EzSGXC4_NqPysVLkhtaqmJ0AmVBh_q2aMWlz_uK-qRumH4buRFshoUOcAMocvQJK0H0ZJksbpMBsmvTTqwhmQKO6H2SDKsjhNRlEWJdmiC19r1144jEdJnMX9pBeno2E8WLwA0IMafA](https://mermaid.live/edit#pako:eNp9kt9O2zAUxl8lOleFlahJ06axKm7gfrueIiETnxZLjl3ZDhrrKm03u92ukXgHxB-BxAavYN4IN21pYNEsxbI_n9_5zjnKHArFEAgUghpzyOlU0zKXgV-1EnzSilWFDeYrcbk-GKu5nAaWW4ENeSIUtcFM82KtLpqJPmqGui2NsdRWpqELbpZpat-mbtAeMRT8FDXqzuHmFLCdFrvtc8NyPKbH3pUWdn__n8LNDJE11LVVZ1W4ajM5UJXm77oqqBBHheAobae1MK0kviEm4uxd5Mpyd2_vdfwkcOfu0f1xT36_c_fPP_33K-hEYbi704SUh7a9e-y3u37-7m7dtbtsQNEa2oaOv3ly05DnLnz8D_fgyRtveeUu3V93725bsVVP_4NyCV2Yas6AWF1hF0rUJV1eoR5FDvYES8yB-CPDCa2EzSGXC4_NqPysVLkhtaqmJ0AmVBh_q2aMWlz_uK-qRumH4buRFshoUOcAMocvQJK0H0ZJksbpMBsmvTTqwhmQKO6H2SDKsjhNRlEWJdmiC19r1144jEdJnMX9pBeno2E8WLwA0IMafA)

**Задание 6**

Придумайте и спроектируйте структуру классов для **Социальной сети**.  
В системе должны быть:

- Пользователь.
- Пост (сообщение).
- Комментарий.

**Условия связей:**

1. Один Пользователь может написать много Постов.
2. Пост жестко привязан к Пользователю (или нет? Решите сами и обоснуйте выбором стрелки).
3. К Посту можно оставлять Комментарии. Если удалить Пост, комментарии тоже должны исчезнуть.

**Требование:** нарисовать схему и добавить короткий комментарий почему вы выбрали именно такие связи

![](file:///C:/Users/gasil/AppData/Local/Temp/msohtmlclip1/01/clip_image012.jpg)  
[https://mermaid.live/edit#pako:eNqNUtFqgzAU_ZVwn7rOiqZWq6_dB-xlL0MowaRWqEmJEboVYU973Z73FYMytoex_UL6R4uxLQ760AiSe84951wTt5AJyiCBbEWq6qYguSRlypFZFkF3FZNo2yHtui64QgXtAZWSBc9RbRo5KVmPySQjis3XolKDTHDFuLrq6KYfcWv4iyIOHj2CGn9VlAx1UXRO-iyhdJ6JsjSagWIb5SBSq6WQ54aYdX0XzdF69VB7RJ3zP2OLp-CngMRoZHae6w5NYb83QfpV7_ZP-kPv9Pv-WX_tXzqZpTvZsC87TmiUb_pHf-tf8_40up722HMSdcGtl53mfGr7gAO5LCgkStbMgZLJkrQl2ANJQS2ZuVtIzJayBalXKoWUN0a2JvxeiPKolKLOl5AsyKoyVb1ur-jwX51QyThlciZqriDxPd-aQLKFDSRBNHb9IIhwFMZh4EWGfDBNeOzGEz-OcRRM_dgP4saBRxvruSGeBjjG48DD0TTEk-YPRk7scg](https://mermaid.live/edit#pako:eNqNUtFqgzAU_ZVwn7rOiqZWq6_dB-xlL0MowaRWqEmJEboVYU973Z73FYMytoex_UL6R4uxLQ760AiSe84951wTt5AJyiCBbEWq6qYguSRlypFZFkF3FZNo2yHtui64QgXtAZWSBc9RbRo5KVmPySQjis3XolKDTHDFuLrq6KYfcWv4iyIOHj2CGn9VlAx1UXRO-iyhdJ6JsjSagWIb5SBSq6WQ54aYdX0XzdF69VB7RJ3zP2OLp-CngMRoZHae6w5NYb83QfpV7_ZP-kPv9Pv-WX_tXzqZpTvZsC87TmiUb_pHf-tf8_40up722HMSdcGtl53mfGr7gAO5LCgkStbMgZLJkrQl2ANJQS2ZuVtIzJayBalXKoWUN0a2JvxeiPKolKLOl5AsyKoyVb1ur-jwX51QyThlciZqriDxPd-aQLKFDSRBNHb9IIhwFMZh4EWGfDBNeOzGEz-OcRRM_dgP4saBRxvruSGeBjjG48DD0TTEk-YPRk7scg)