import json
import os
from dataclasses import dataclass
from typing import Dict, List, Optional
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
from enum import Enum
import math  # Добавляем импорт math

class DeviceType(Enum):
    ROUTER = "router"
    SWITCH = "switch"
    SERVER = "server"
    PC = "pc"
    FIREWALL = "firewall"
    PRINTER = "printer"
    ACCESS_POINT = "access_point"

@dataclass
class NetworkDevice:
    id: str
    name: str
    device_type: DeviceType
    ip_address: Optional[str] = None
    vendor: Optional[str] = None
    model: Optional[str] = None
    x: float = 0.0
    y: float = 0.0

@dataclass
class Connection:
    source_id: str
    target_id: str
    bandwidth: str = "1Gbps"
    connection_type: str = "ethernet"
    color: str = "black"

class NetworkDiagramGenerator:
    def __init__(self, title: str = "Сетевая диаграмма"):
        self.devices: Dict[str, NetworkDevice] = {}
        self.connections: List[Connection] = []
        self.title = title
        self.fig, self.ax = plt.subplots(figsize=(16, 12))
        
    def add_device(self, device: NetworkDevice):
        """Добавить сетевое устройство"""
        self.devices[device.id] = device
        
    def add_connection(self, connection: Connection):
        """Добавить соединение между устройствами"""
        self.connections.append(connection)
    
    def auto_layout(self):
        """Автоматическое расположение устройств на схеме"""
        num_devices = len(self.devices)
        if num_devices == 0:
            return
            
        # Разделяем устройства по типам для лучшей организации
        routers = [d for d in self.devices.values() if d.device_type == DeviceType.ROUTER]
        switches = [d for d in self.devices.values() if d.device_type == DeviceType.SWITCH]
        servers = [d for d in self.devices.values() if d.device_type == DeviceType.SERVER]
        others = [d for d in self.devices.values() if d.device_type not in 
                  [DeviceType.ROUTER, DeviceType.SWITCH, DeviceType.SERVER]]
        
        # Располагаем маршрутизаторы в центре
        center_x, center_y = 0, 0
        radius = 5
        
        for i, router in enumerate(routers):
            angle = 2 * math.pi * i / max(len(routers), 1)
            router.x = center_x + radius * math.cos(angle)
            router.y = center_y + radius * math.sin(angle)
        
        # Располагаем коммутаторы вокруг маршрутизаторов
        switch_radius = radius + 3
        for i, switch in enumerate(switches):
            angle = 2 * math.pi * i / max(len(switches), 1)
            switch.x = center_x + switch_radius * math.cos(angle)
            switch.y = center_y + switch_radius * math.sin(angle)
        
        # Располагаем серверы в верхней части
        for i, server in enumerate(servers):
            server.x = -8 + (i * 3)
            server.y = 8
        
        # Располагаем остальные устройства в нижней части
        for i, device in enumerate(others):
            device.x = -10 + (i * 3)
            device.y = -8
    
    def draw_device(self, device: NetworkDevice):
        """Нарисовать одно устройство"""
        colors = {
            DeviceType.ROUTER: '#4CAF50',      # Зеленый
            DeviceType.SWITCH: '#2196F3',      # Синий
            DeviceType.SERVER: '#FF9800',      # Оранжевый
            DeviceType.PC: '#9E9E9E',         # Серый
            DeviceType.FIREWALL: '#F44336',   # Красный
            DeviceType.PRINTER: '#9C27B0',    # Фиолетовый
            DeviceType.ACCESS_POINT: '#00BCD4' # Голубой
        }
        
        color = colors.get(device.device_type, '#9E9E9E')
        
        # Рисуем устройство в зависимости от типа
        if device.device_type == DeviceType.ROUTER:
            # Круг для маршрутизатора
            patch = patches.Circle(
                (device.x, device.y), 0.8,
                facecolor=color, edgecolor='black',
                linewidth=2, alpha=0.9
            )
        elif device.device_type == DeviceType.SWITCH:
            # Квадрат для коммутатора
            patch = patches.Rectangle(
                (device.x - 0.7, device.y - 0.7), 1.4, 1.4,
                facecolor=color, edgecolor='black',
                linewidth=2, alpha=0.9
            )
        elif device.device_type == DeviceType.SERVER:
            # Ромб для сервера (квадрат повернутый на 45 градусов)
            diamond = patches.RegularPolygon(
                (device.x, device.y), 4, radius=0.8,
                facecolor=color, edgecolor='black',
                linewidth=2, alpha=0.9
            )
            # Поворачиваем ромб
            diamond.set_transform(
                diamond.get_transform() + 
                mpatches.transforms.Affine2D().rotate_deg(45).translate(0, 0)
            )
            self.ax.add_patch(diamond)
            
            # Добавляем текст с именем устройства
            self.ax.text(
                device.x, device.y - 1.2,
                device.name,
                ha='center', va='top',
                fontsize=9, fontweight='bold',
                bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.7)
            )
            
            # Добавляем IP-адрес если есть
            if device.ip_address:
                self.ax.text(
                    device.x, device.y - 1.8,
                    device.ip_address,
                    ha='center', va='top',
                    fontsize=8, style='italic',
                    bbox=dict(boxstyle="round,pad=0.2", facecolor="lightyellow", alpha=0.7)
                )
            return  # Выходим раньше, так как уже добавили патч
            
        elif device.device_type == DeviceType.PC:
            # Треугольник для ПК
            patch = patches.RegularPolygon(
                (device.x, device.y), 3, radius=0.8,
                facecolor=color, edgecolor='black',
                linewidth=2, alpha=0.9
            )
        elif device.device_type == DeviceType.FIREWALL:
            # Шестиугольник для файрвола
            patch = patches.RegularPolygon(
                (device.x, device.y), 6, radius=0.8,
                facecolor=color, edgecolor='black',
                linewidth=2, alpha=0.9
            )
        elif device.device_type == DeviceType.PRINTER:
            # Пятиугольник для принтера
            patch = patches.RegularPolygon(
                (device.x, device.y), 5, radius=0.8,
                facecolor=color, edgecolor='black',
                linewidth=2, alpha=0.9
            )
        elif device.device_type == DeviceType.ACCESS_POINT:
            # Круг с волнами для точки доступа
            patch = patches.Circle(
                (device.x, device.y), 0.8,
                facecolor=color, edgecolor='black',
                linewidth=2, alpha=0.9
            )
            # Добавляем концентрические круги для эффекта волн
            for r in [1.2, 1.6]:
                wave = patches.Circle(
                    (device.x, device.y), r,
                    fill=False, edgecolor=color,
                    linewidth=1, alpha=0.3, linestyle='--'
                )
                self.ax.add_patch(wave)
        else:
            # По умолчанию - круг
            patch = patches.Circle(
                (device.x, device.y), 0.8,
                facecolor=color, edgecolor='black',
                linewidth=2, alpha=0.9
            )
        
        self.ax.add_patch(patch)
        
        # Добавляем текст с именем устройства
        self.ax.text(
            device.x, device.y - 1.2,
            device.name,
            ha='center', va='top',
            fontsize=9, fontweight='bold',
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.7)
        )
        
        # Добавляем IP-адрес если есть
        if device.ip_address:
            self.ax.text(
                device.x, device.y - 1.8,
                device.ip_address,
                ha='center', va='top',
                fontsize=8, style='italic',
                bbox=dict(boxstyle="round,pad=0.2", facecolor="lightyellow", alpha=0.7)
            )
    
    def draw_connection(self, connection: Connection):
        """Нарисовать соединение между устройствами"""
        source = self.devices.get(connection.source_id)
        target = self.devices.get(connection.target_id)
        
        if not source or not target:
            return
        
        # Определяем стиль линии в зависимости от типа соединения
        line_styles = {
            'ethernet': '-',
            'fiber': '--',
            'wireless': ':',
            'wan': '-.'
        }
        
        line_style = line_styles.get(connection.connection_type, '-')
        
        # Рисуем линию соединения
        line = mlines.Line2D(
            [source.x, target.x],
            [source.y, target.y],
            color=connection.color,
            linewidth=2,
            linestyle=line_style,
            alpha=0.7
        )
        
        self.ax.add_line(line)
        
        # Добавляем метку с пропускной способностью
        mid_x = (source.x + target.x) / 2
        mid_y = (source.y + target.y) / 2
        
        self.ax.text(
            mid_x, mid_y,
            connection.bandwidth,
            ha='center', va='center',
            fontsize=8,
            bbox=dict(boxstyle="round,pad=0.2", facecolor="white", alpha=0.8),
            rotation=15
        )
    
    def draw_legend(self):
        """Создать легенду диаграммы"""
        legend_elements = []
        
        # Устройства
        device_colors = {
            DeviceType.ROUTER: ('Маршрутизатор', '#4CAF50'),
            DeviceType.SWITCH: ('Коммутатор', '#2196F3'),
            DeviceType.SERVER: ('Сервер', '#FF9800'),
            DeviceType.PC: ('ПК', '#9E9E9E'),
            DeviceType.FIREWALL: ('Файрвол', '#F44336'),
            DeviceType.PRINTER: ('Принтер', '#9C27B0'),
            DeviceType.ACCESS_POINT: ('Точка доступа', '#00BCD4')
        }
        
        for device_type, (label, color) in device_colors.items():
            patch = mpatches.Patch(
                color=color,
                label=label,
                alpha=0.9
            )
            legend_elements.append(patch)
        
        # Соединения
        line_styles = [
            ('Ethernet', '-', 'black'),
            ('Оптоволокно', '--', 'blue'),
            ('Wi-Fi', ':', 'green'),
            ('WAN', '-.', 'red')
        ]
        
        for name, style, color in line_styles:
            line = mlines.Line2D(
                [], [],
                color=color,
                linestyle=style,
                linewidth=2,
                label=name
            )
            legend_elements.append(line)
        
        # Добавляем легенду
        self.ax.legend(
            handles=legend_elements,
            loc='upper left',
            bbox_to_anchor=(1.05, 1),
            borderaxespad=0.,
            fontsize=9,
            title="Условные обозначения",
            title_fontsize=10
        )
    
    def generate(self):
        """Сгенерировать полную диаграмму"""
        # Автоматическое расположение устройств
        self.auto_layout()
        
        # Рисуем все соединения
        for connection in self.connections:
            self.draw_connection(connection)
        
        # Рисуем все устройства (поверх соединений)
        for device in self.devices.values():
            self.draw_device(device)
        
        # Настройки графика
        self.ax.set_title(self.title, fontsize=16, fontweight='bold', pad=20)
        self.ax.set_aspect('equal')
        self.ax.autoscale_view()
        
        # Убираем оси
        self.ax.axis('off')
        
        # Добавляем легенду
        self.draw_legend()
        
        # Настраиваем отступы
        plt.tight_layout()
    
    def export_png(self, filename: str = "network_diagram.png", dpi: int = 300):
        """Экспортировать в PNG"""
        plt.savefig(filename, dpi=dpi, bbox_inches='tight', facecolor='white')
        print(f"✓ Диаграмма сохранена как {filename}")
    
    def export_pdf(self, filename: str = "network_diagram.pdf"):
        """Экспортировать в PDF"""
        plt.savefig(filename, format='pdf', bbox_inches='tight')
        print(f"✓ Диаграмма сохранена как {filename}")
    
    def export_svg(self, filename: str = "network_diagram.svg"):
        """Экспортировать в SVG"""
        plt.savefig(filename, format='svg', bbox_inches='tight')
        print(f"✓ Диаграмма сохранена как {filename}")
    
    def save_config(self, filename: str = "network_config.json"):
        """Сохранить конфигурацию сети в JSON"""
        config = {
            "title": self.title,
            "devices": [
                {
                    "id": device.id,
                    "name": device.name,
                    "type": device.device_type.value,
                    "ip_address": device.ip_address,
                    "vendor": device.vendor,
                    "model": device.model,
                    "x": device.x,
                    "y": device.y
                }
                for device in self.devices.values()
            ],
            "connections": [
                {
                    "source_id": conn.source_id,
                    "target_id": conn.target_id,
                    "bandwidth": conn.bandwidth,
                    "connection_type": conn.connection_type,
                    "color": conn.color
                }
                for conn in self.connections
            ]
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        print(f"✓ Конфигурация сохранена как {filename}")
    
    def load_config(self, filename: str):
        """Загрузить конфигурацию сети из JSON"""
        with open(filename, 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        self.title = config.get("title", "Сетевая диаграмма")
        self.devices.clear()
        self.connections.clear()
        
        # Загружаем устройства
        for device_data in config.get("devices", []):
            device = NetworkDevice(
                id=device_data["id"],
                name=device_data["name"],
                device_type=DeviceType(device_data["type"]),
                ip_address=device_data.get("ip_address"),
                vendor=device_data.get("vendor"),
                model=device_data.get("model"),
                x=device_data.get("x", 0.0),
                y=device_data.get("y", 0.0)
            )
            self.add_device(device)
        
        # Загружаем соединения
        for conn_data in config.get("connections", []):
            connection = Connection(
                source_id=conn_data["source_id"],
                target_id=conn_data["target_id"],
                bandwidth=conn_data.get("bandwidth", "1Gbps"),
                connection_type=conn_data.get("connection_type", "ethernet"),
                color=conn_data.get("color", "black")
            )
            self.add_connection(connection)
        
        print(f"✓ Конфигурация загружена из {filename}")

def create_example_network():
    """Создать пример корпоративной сети"""
    generator = NetworkDiagramGenerator("Корпоративная сеть компании 'ТехноКорп'")
    
    # Добавляем основные устройства
    devices = [
        NetworkDevice("r1", "Основной маршрутизатор", DeviceType.ROUTER, "192.168.1.1", "Cisco", "ISR 4331"),
        NetworkDevice("fw1", "Файрвол", DeviceType.FIREWALL, "192.168.1.2", "Fortinet", "FortiGate 100F"),
        NetworkDevice("sw1", "Ядровой коммутатор", DeviceType.SWITCH, "192.168.1.3", "Cisco", "Catalyst 9300"),
        NetworkDevice("sw2", "Распределительный коммутатор", DeviceType.SWITCH, "192.168.1.4", "Cisco", "Catalyst 9200"),
        NetworkDevice("sw3", "Коммутатор офиса", DeviceType.SWITCH, "192.168.1.5"),
        NetworkDevice("srv1", "Файловый сервер", DeviceType.SERVER, "192.168.1.10", "Dell", "PowerEdge R740"),
        NetworkDevice("srv2", "Сервер БД", DeviceType.SERVER, "192.168.1.11", "HP", "ProLiant DL380"),
        NetworkDevice("srv3", "Веб-сервер", DeviceType.SERVER, "192.168.1.12"),
        NetworkDevice("ap1", "Точка доступа 1", DeviceType.ACCESS_POINT, "192.168.1.20"),
        NetworkDevice("ap2", "Точка доступа 2", DeviceType.ACCESS_POINT, "192.168.1.21"),
        NetworkDevice("pc1", "Рабочая станция 1", DeviceType.PC, "192.168.1.100"),
        NetworkDevice("pc2", "Рабочая станция 2", DeviceType.PC, "192.168.1.101"),
        NetworkDevice("pc3", "Рабочая станция 3", DeviceType.PC, "192.168.1.102"),
        NetworkDevice("pr1", "Сетевой принтер", DeviceType.PRINTER, "192.168.1.50", "HP", "LaserJet MFP")
    ]
    
    for device in devices:
        generator.add_device(device)
    
    # Добавляем соединения
    connections = [
        Connection("r1", "fw1", "10Gbps", "fiber", "blue"),
        Connection("fw1", "sw1", "10Gbps", "fiber", "blue"),
        Connection("sw1", "sw2", "10Gbps", "ethernet", "black"),
        Connection("sw1", "srv1", "1Gbps", "ethernet", "green"),
        Connection("sw1", "srv2", "1Gbps", "ethernet", "green"),
        Connection("sw2", "sw3", "1Gbps", "ethernet", "black"),
        Connection("sw2", "srv3", "1Gbps", "ethernet", "green"),
        Connection("sw2", "pr1", "100Mbps", "ethernet", "purple"),
        Connection("sw3", "ap1", "1Gbps", "ethernet", "orange"),
        Connection("sw3", "ap2", "1Gbps", "ethernet", "orange"),
        Connection("sw3", "pc1", "100Mbps", "ethernet", "gray"),
        Connection("sw3", "pc2", "100Mbps", "ethernet", "gray"),
        Connection("ap1", "pc3", "300Mbps", "wireless", "red"),
        Connection("r1", "internet", "1Gbps", "wan", "red")
    ]
    
    # Добавляем виртуальное устройство "интернет"
    internet_device = NetworkDevice("internet", "Интернет", DeviceType.ROUTER)
    internet_device.x = 10
    internet_device.y = 0
    generator.add_device(internet_device)
    
    for connection in connections:
        generator.add_connection(connection)
    
    return generator

def main():
    """Основная функция"""
    print("=" * 60)
    print("ГЕНЕРАТОР СЕТЕВЫХ ДИАГРАММ")
    print("=" * 60)
    
    try:
        # Создаем пример сети
        generator = create_example_network()
        
        # Генерируем диаграмму
        print("\nГенерация сетевой диаграммы...")
        generator.generate()
        
        # Экспортируем в различные форматы
        print("\nЭкспорт диаграммы:")
        generator.export_png("corporate_network.png")
        generator.export_pdf("corporate_network.pdf")
        generator.export_svg("corporate_network.svg")
        
        # Сохраняем конфигурацию
        generator.save_config("network_config.json")
        
        print("\n✓ Диаграмма успешно создана из JSON!")
        print("\nСозданные файлы:")
        print("  - corporate_network.png")
        print("  - corporate_network.pdf")
        print("  - corporate_network.svg")
        print("  - network_config.json")
        
        # Показываем диаграмму
        plt.show()
        
    except Exception as e:
        print(f"\n✗ Ошибка: {e}")
        print("\nУстановите необходимые библиотеки:")
        print("pip install matplotlib")
        return 1
    return 0

if __name__ == "__main__":
    exit(main())