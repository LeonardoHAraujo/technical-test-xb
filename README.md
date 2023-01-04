# Technical test (Rafa Milk)

Hello, first I would like to thank you for the opportunity and I hope you like the content developed,
because it was with affection and dedication that I performed this test.

## Client

For the client side of the application, an application was created using [Typescript](https://www.typescriptlang.org/)
and [Context Api](https://reactjs.org/docs/context.html) for data state management.
Responsiveness was applied to all screens, aiming at a better user experience
and the concept of `Components` from ReactJs was applied, which allows us to reuse screens
in several places. So it was used in the translation component.

![React](https://reactjs.org/logo-og.png)

## Server

On the server side, a simple `API` in `Flask` and `MongoDB` following market patterns
like `Factory`, `Dependency injection`, principles of `SOLID` and among other abstractions.

As the main architecture on which the `API` was built, we have the famous [Clean Archtecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
from [Uncle Bob](https://en.wikipedia.org/wiki/Robert_C._Martin) which itself abstracts in layers
the different responsibilities of an application. Therefore, the data layer (DB)
is completely separated from the application domain rule and so we have several gains from this,
such as easy maintenance, project scalability and among others.

Architecture illustration:

![clean arch](https://blog.cleancoder.com/uncle-bob/images/2012-08-13-the-clean-architecture/CleanArchitecture.jpg)

## Challenge

So let's go! The proposed challenge was to develop a full-stack application, with
a client with some market JS framework and a server for login control,
using Flask or Django as a python framework and a database to complement
of the application. The application must contain the following features:

- User registration;
- Login/logout system;
- Form validations;
- Translation with external dependency;
- Client/Server Interaction;
- Responsive layout;

### User registration

User registration is maintained by the `API` through the `POST - /users/create` endpoint.

Your `payload` is:

```json
{
    "name": "Leonardo",
    "email": "ledharaujo@gmail.com",
    "password": "123456"
}
```

### Login/logout system

For this case, two endpoints were created.

- `POST - /jwt/auth`: Which authenticates the created user and returns a token [JWT](https://jwt.io/) valid for 5 minutes.
- `GET - /jwt/verify/{token}`: Which receives the token from the client and returns whether it is valid or not.

Follows `payload` from the endpoint `POST - /jwt/auth`:

```json
{
    "email": "ledharaujo@gmail.com",
    "password": "123456"
}
```

### Form validations

A library called [Ant](https://ant.design/) to perform the componentization
of the client elements and this library was essential for validating the form fields.

### Translation with external dependency

To carry out the system translation, an external dependency called [I18n](https://www.i18next.com/) was used,
which brings validity in development, low cost compared to a translation api for example
and not to mention the gain in control over the texts that are translated, which is why the choice
of this solution.

### Client/Server Interaction

In the client and server interaction, we use the library [Axios](https://axios-http.com/docs/intro)
with the combination of [Context Api](https://reactjs.org/docs/context.html) and browser `LocalStorage`
for operating the login/logout system and receiving data.

### Responsive layout

To make the layout fully responsive, we used [CSS Media Query](https://www.w3schools.com/css/css3_mediaqueries.asp)
for adapting the components to different screen sizes.

## How to run the project

Talking about the api features is very good, but I need to explain
how to run the project. So let's go!

First of all, I need you to have three very important resources on your machine.
Important for this project:

- [Docker](https://docs.docker.com/desktop/linux/install/)
- [Docker compose](https://docs.docker.com/compose/install/)
- [Yarn](https://classic.yarnpkg.com/lang/en/docs/install/#debian-stable)

If everything is ok, let's get started.

#### Server

First we need to run the application on the server side, as the client depends on it.
The `Server` application is orchestrated by a `docker-compose`, so follow the steps
below:

- Clone the repository on your machine.
- Go to the `server` folder with the command: `cd server/`
- Rename the `.env.example` file to `.env`, with the command:
    - `mv .env.example .env`
- Now just run this command to bring up the container orchestra.
    - `docker-compose up --build -d`

After that the api will be running on `http://127.0.0.1:5000`

#### Client

To run the client-side application, it's as simple as, just follow
the steps below:

- Go to the `client` folder with the command: `cd ../client/`
- To install the dependencies, run the command:
    - `yarn`
- And finally, just run the command:
    - `yarn dev`

After that the client will be running on `http://localhost:5173/`

