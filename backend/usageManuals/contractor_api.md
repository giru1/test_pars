# <div id="main">EfiritPro Retail ContractorModule ContractorAPI</div>

## <div id="content">Содержание</div>

- [ContractorAPI](#main)
    - [Содержание](#content)
    - [Использование](#usage)
        - [Получение списка контрагентов](#usage-get-list)
        - [Получение информации о контрагенте](#usage-get)
        - [Создание контрагента](#usage-create)
        - [Изменение контрагента](#usage-change)
        - [Удаление контрагента](#usage-remove)

## <div id="usage">Использование</div>

### <div id="usage-get-list">Получение списка контрагентов</div>

#### API Endpoint
HttpGet [apiHost]/contractor/getContractors

#### Ограничения

- В Headers есть поле Authorization с токеном "Bearer [token]"
- Совпадают ownerId в токене и запросе
- Совпадают organizationId в токене и запросе (для работников)
- В токене есть разрешение /contractor/getContractors (для работников)

#### Request

```
Query
{
    "ownerId": string,         | обязательное
    "organizationId": string    | обязательное
    "hidden": bool | null       | не обязательное
}
```

####  Response 401 (Пользователь без токена)
####  Response 403 (Пользователь не прошёл ограничения)
####  Response 200
```
Body
Content-Type: "application/json"
{
    "contractors": [
        {
            "id": string,
            "name": string,
            "type": number,
            "hidden": bool,
        }, ...
    ],
}
```

### <div id="usage-get">Получение информации о контрагенте</div>

#### API Endpoint
HttpGet [apiHost]/contractor/getContractor

#### Ограничения

- В Headers есть поле Authorization с токеном "Bearer [token]"
- Совпадают ownerId в токене и запросе
- Совпадают organizationId в токене и запросе (для работников)
- В токене есть разрешение /contractor/getContractor (для работников)

#### Request

```
Query
{
    "ownerId": string,         | обязательное
    "organizationId": string,   | обязательное
    "contractorId": string      | обязательное
}
```

####  Response 401 (Пользователь без токена)
####  Response 403 (Пользователь не прошёл ограничения)
####  Response 404 (Контрагент не найден)
####  Response 200
```
Body
Content-Type: "application/json"
{
    "id": string,
    "name": string,
    "type": number,
    "ownerId": string,
    "organizationId": string,
    "tin": string | null,
    "rrc": string | null,
    "legalAddress": string | null,
    "actualAddress": string | null,
    "phone": string | null,
    "email": string | null,
    "hidden": bool,
}
```

### <div id="usage-create">Создание контрагента</div>

#### API Endpoint
HttpGet [apiHost]/contractor/createContractor

#### Ограничения

- В Headers есть поле Authorization с токеном "Bearer [token]"
- Совпадают ownerId в токене и запросе
- Совпадают organizationId в токене и запросе (для работников)
- В токене есть разрешение /contractor/createContractor (для работников)

#### Request

```
Query
{
    "ownerId": string,         | обязательное
    "organizationId": string,   | обязательное
}
Body
Content-Type: "application/json"
{
    "name": string,                 | обязательное
    "typeId": string,               | обязательное
    "tin": string | null,
    "rrc": string | null,
    "legalAddress": string | null,
    "actualAddress": string | null,
    "phone": string | null,
    "email": string | null,
    "hidden": bool | null           | по умолчанию False
}
```

####  Response 401 (Пользователь без токена)
####  Response 403 (Пользователь не прошёл ограничения)
####  Response 500 (Если контрагента не удалось создать)
####  Response 200
```
Body
Content-Type: "application/json"
{
    "id": string,
    "name": string,
    "type": number,
    "ownerId": string,
    "organizationId": string,
    "tin": string | null,
    "rrc": string | null,
    "legalAddress": string | null,
    "actualAddress": string | null,
    "phone": string | null,
    "email": string | null,
    "hidden": bool,
}
```

### <div id="usage-change">Изменение контрагента</div>

#### API Endpoint
HttpGet [apiHost]/contractor/changeContractor

#### Ограничения

- В Headers есть поле Authorization с токеном "Bearer [token]"
- Совпадают ownerId в токене и запросе
- Совпадают organizationId в токене и запросе (для работников)
- В токене есть разрешение /contractor/changeContractor (для работников)

#### Request

```
Query
{
    "ownerId": string,         | обязательное
    "organizationId": string,   | обязательное
    "contractorId": string      | обязательное
}
Body
Content-Type: "application/json"
{
    "name": string | null,
    "typeId": string | null,
    "tin": string | null,
    "rrc": string | null,
    "legalAddress": string | null,
    "actualAddress": string | null,
    "phone": string | null,
    "email": string | null,
    "hidden": bool | null,
}
```

####  Response 401 (Пользователь без токена)
####  Response 403 (Пользователь не прошёл ограничения)
####  Response 404 (Если контрагента не удалось изменить)
####  Response 200
```
Body
Content-Type: "application/json"
{
    "id": string,
    "name": string,
    "type": number,
    "ownerId": string,
    "organizationId": string,
    "tin": string | null,
    "rrc": string | null,
    "legalAddress": string | null,
    "actualAddress": string | null,
    "phone": string | null,
    "email": string | null,
    "hidden": bool,
}
```

### <div id="usage-remove">Удаление контрагента</div>

#### API Endpoint
HttpGet [apiHost]/contractor/removeContractor

#### Ограничения

- В Headers есть поле Authorization с токеном "Bearer [token]"
- Совпадают ownerId в токене и запросе
- Совпадают organizationId в токене и запросе (для работников)
- В токене есть разрешение /contractor/removeContractor (для работников)

#### Request

```
Query
{
    "ownerId": string,         | обязательное
    "organizationId": string,   | обязательное
    "contractorId": string      | обязательное
}
```

####  Response 401 (Пользователь без токена)
####  Response 403 (Пользователь не прошёл ограничения)
####  Response 404 (Если контрагента не удалось удалить)
####  Response 200
```
Body
Content-Type: "application/json"
{
    "id": string,
    "name": string,
    "type": number,
    "ownerId": string,
    "organizationId": string,
    "tin": string | null,
    "rrc": string | null,
    "legalAddress": string | null,
    "actualAddress": string | null,
    "phone": string | null,
    "email": string | null,
    "hidden": bool,
}
```