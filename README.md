## Bottlegram

Free "social media" platform without any accounts\
The UI may not be that cool but it's free and open source

## What can it do?
You can make posts for other to see\
Comment some other posts made by other people

## What I want to add
I want to add messaging function with personal encryption keys

To chat you will need to write another username and the encryption key with that your messages will be encrypted

## Why I made this
I made this app because I wanted to make a platform\
that doesnt require you to make accounts and shit like this

I wanted to create an app that is 100% free and anyone can use without restrictions

## Technologies
It uses python with flask on the server side\
And svelte at the frontend side

As database it uses sqlite3

For generating random usernames it uses [this library](https://www.npmjs.com/package/random-words?activeTab=readme)

## Links

Here are two links with the demo\
[First link](https://bottlegram.vercel.app/) and [the second](https://bottlegram.rf.gd/)

To use it you need to start the server by yourself on your pc

[Here](https://venddair.pythonanywhere.com/) are the demo server to test the app\
Just copy the link at paste in the app to test it

## Some Pictures of the app

Main Page with posts
![s](screenshots/1.png)

An example of post
![s](screenshots/3.png)

Make new post page
![s](screenshots/4.png)

## How to start it

First of all we need an server

To start a server type:
```
cd server
pip3 install flask flask_cors
flask run
```

After we started the server we need a client to interact with that server
```
cd client
npm install
npm run dev
```

After we launch the client launch it and paste the url for the server that we created\
By default its [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
