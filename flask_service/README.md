# HOW TO RUN FLASK API
In path `~/flask_service/` run below command
```
python ./app.py
```

# API description
## users
### model
```
{
    "id": string,
    "name": string,
    "lastname": string,
    "role": string
}
```
### URLs
#### get all users
* method: GET
* path: /users

Responses:
* 200 OK

Body:
* application/json
```
[
    {
        "id": "atest",
        "name": "api",
        "lastname": "test",
        "role": "NONE"
    }
]
```
* application/xml
```
<users>
    <user>
        <id>"atest"</id>,
        <name>"api"</name>,
        <lastname>"test"</lastname>,
        <role>"NONE"</role>
    </user>
</users>
```

#### get user by id
* method: GET
* path: /users/<user_id>
* headers: accept (application/json|application/xml, default: application/json)

Responses:
* 200 OK

Body:
* application/json
```
{
    "id": "atest",
    "name": "api",
    "lastname": "test",
    "role": "NONE"
}
```
* application/xml
```
<user>
    <id>"atest"</id>,
    <name>"api"</name>,
    <lastname>"test"</lastname>,
    <role>"NONE"</role>
</user>
```

* 404 NOT FOUND

Body:
```
{
    "error": "Not Found",
    "message": "User atestowy not found!"
}
```

#### create new user
* method: POST
* path: /users
* headers: content-type (application/json), accept (application/json|application/xml, default: application/json)
* body:
```
{
    "name"(required): string,
    "lastname"(required): string,
    "role"(optional): string(from /roles, default: NONE)
}
```

Responses:
* 201 CREATED

Body:
* application/json
```
{
    "id": "atest",
    "name": "api",
    "lastname": "test",
    "role": "NONE"
}
```
* application/xml
```
<user>
    <id>"atest"</id>,
    <name>"api"</name>,
    <lastname>"test"</lastname>,
    <role>"NONE"</role>
</user>
```

* 400 BAD REQUEST

Body:
* application/json
```
{
    "error": "Bad request",
    "message": "Lack of required data in body: {'lastname', 'name'}!"
}
```

* 404 NOT FOUND

Body:
```
{
    "error": "Not Found",
    "message": "User atestowy not found!"
}
```

* 422 UNPROCESSABLE ENTITY

Body:
* application/json
```
{
    "error": "Unprocessable entity",
    "message": "Incorrect content type: application/xml!"
}
```

#### update user
* method: PUT
* path: /users/<user_id>
* headers: content-type (application/json), accept (application/json|application/xml, default: application/json)
* body:
```
{
    "name"(required): string,
    "lastname"(required): string,
    "role"(optional): string(from /roles, default: NONE)
}
```

Responses:
* 200 OK

Body:
* application/json
```
{
    "id": "atest",
    "name": "api",
    "lastname": "test",
    "role": "NONE"
}
```
* application/xml
```
<user>
    <id>"atest"</id>,
    <name>"api"</name>,
    <lastname>"test"</lastname>,
    <role>"NONE"</role>
</user>
```

* 400 BAD REQUEST

Body:
* application/json
```
{
    "error": "Bad request",
    "message": "Lack of required data in body: {'lastname', 'name'}!"
}
```

* 422 UNPROCESSABLE ENTITY

Body:
* application/json
```
{
    "error": "Unprocessable entity",
    "message": "Incorrect content type: application/xml!"
}
```

## roles
### model
```
{
    "name": string,
    "description": string
}
```
### URLs
#### get all roles
* method: GET
* path: /roles

Responses:
* 200 OK

Body:
* application/json
```
[
    "NONE",
    "VIEWER",
    "MODERATOR",
    "ADMIN"
]
```
* application/xml
```
<roles>
	<role>NONE</role>
	<role>VIEWER</role>
	<role>MODERATOR</role>
	<role>ADMIN</role>
</roles>
```

#### get role by id
* method: GET
* path: /roles/<role_id>
* headers: accept (application/json|application/xml, default: application/json)

Responses:
* 200 OK

Body:
* application/json
```
{
    "description": "For admit content and service.",
    "name": "Admin"
}
```
* application/xml
```
<role>
	<name>Admin</name>
	<description>For admit content and service.</description>
</role>
```

* 404 NOT FOUND

Body:
```
{
    "error": "Not Found",
    "message": "Role testowa not found!"
}
```


