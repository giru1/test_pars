# <div id="main">EfiritPro Retail ContractorModule - Модуль контрагентов</div>

## <div id="content">Содержание</div>

- [ContractorModule](#main)
    - [Содержание](#content)
    - [Предназначение](#target)
    - [Установка](#install)
    - [Использование](#usage)

## <div id="target">Предназначение</div>

Модуль ответственен за создание, удаление, изменение контрагентов клиента.

## <div id="install">Установка</div>

### Предварительные требования

- docker версии ^24.0.0

### Процесс установки

1. Создать образ модуля

```bash
docker build -t efirit-contractor-module:0.1 .
```

2. Применить этот образ в проекте EfiritPro Retail Backend

## <div id="usage">Использование</div>

### Внешнее API

apiHost - http адрес API сервера

- [Contractor API](usageManuals/contractor_api.md)

### RabbitMQ

#### Прослушиваемые очереди и их объекты (см. Miro)

- contractor/eventAck => RabbitEvent
- contractor/removeOrganization => OrganizationEvent

#### Отправляемые очереди и их объекты (см. Miro)
