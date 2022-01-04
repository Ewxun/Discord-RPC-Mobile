# Discord Custom Rich Presence

Allows you to set your own Discord rich presence on **\*any platform**!

\*Assuming that your device has and can run Python 3.5.3 and above, mobile devices can use it on [Replit](https://www.replit.com)

Requirements
--

There are a few packages that are needed for this project to work.

- [pyyaml](https://github.com/yaml/pyyaml.org)
- [discord.py rewrite](https://github.com/Rapptz/discord.py)

Run one of the following to install the packages on your local device.

```console
pip install discord.py pyyaml
```
```console
pip install -r requirements.txt
```

Registering and setting up for an application
--

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications) and login if you have not already do so.
2. Click on `New Application` on the right top corner of the webpage.
3. Enter a name of your choice, any name will do. It will **not** be needed for the project to work.
4. Scroll down till you see `APPLICATION ID`, copy the ID and paste it into the `application_id` field of the [config.yml](config.yml) file.
5. Go to the `Rich Presence` tab and click `Art Assets`
6. At the bottom of the page you can add images by clicking `Add Images`. After adding the images rename them so it is easy for you to remember them. The name of the images will be the image key of the image.
7. Remember to save the changes after adding the images[^img].

[^img]: You can't close or refresh the browser immediatly after saving the changes. This will remove your uploaded images. You have to wait for a few minutes. (due to Discord's caching?)

Configuration
--
All configs are made in the [config.yml](config.yml) file.

### Main

| Config Field | Value Type | Description | Nullable/Blankable |
| --- | :---: | --- | :---: |
| replit | boolean | Whether if you are using Replit or any other services like Replit (not recommended) which provides auto package install | No |
| auth_token | string | Your Discord authorization token | No |
| application_id | int | The ID of the application that you can register through the [Discord Developer Portal](https://discord.com/developers/applications) for art assets. | Yes |
| game | string | The name of the game you want to be displayed | No |
| details | string | Line 2 of the rich presence | Yes |
| state | string | Line 3 of the rich presence | Yes |

### Party

| Config Field | Value Type | Description | Nullable/Blankable |
| --- | :---: | --- | :---: |
| enable_party | boolean | Whether to enable the party. | No |
| party_max_size | int | The number on the right of the party | No |
| party_current_size | int | The left number of the party | No |

#### Minecraft
Uses the party field in the rich presence as the server player count.

| Config Field | Value Type | Description | Nullable/Blankable |
| --- | :---: | --- | :---: |
| enable_detection | boolean | Whether to check for server players | No |
|server_ip|string|The server IP to check (Do not put the port here)| No |
|server_port|int|The server port|Yes (If using the default port (25565))|

### Elapsed Time
| Config Field | Value Type | Description | Nullable/Blankable |
| --- | :---: | --- | :---: |
|enable_elapsed_time|boolean|Whether to enable elapsed time|No|
|mode|string (normal, countdown, custom_start)|What type of display mode to use for the rich presence|No|
|start_time|int(for now)|Input Unix Timstamp for a custom elasped start time for the presence. Eg. If you want it to display `2:00:00 elapsed` subtract 7200 from the [current Unix Timestamp](https://www.unixtimestamp.com/)|No (if `mode` is `custom_start`)|
|end_time|int(for now)|Input Unix Timstamp for a custom elasped end time for the presence. Eg. If you want it to display `2:00:00 left` add 7200 to the [current Unix Timestamp](https://www.unixtimestamp.com/)|No (if `mode` is `countdown`)|

### Images
| Config Field | Value Type | Description | Nullable/Blankable |
| --- | :---: | --- | :---: |
|enable_images|boolean|Whether to use images for the presence|No|
|large_image_key|string|The image key for the large image of the presence|Yes|
|small_image_key|string|The image key for the small image of the presence|Yes|
|large_image_text|string|Text to display when hovering over the large image|Yes|
|small_image_text|string|Text to display when hovering over the small image.|Yes|


Mobile/Replit Users
---
This script adds support for mobile users to use the presence without having to install any external applications. You just have to register for an account at [replit.com](https://replit.com).

### Get your Discord Authorization Token
1. Create a bookmark in your browser(preferably Chrome) of any webpage and name it `Token` or any name you want.
2. Next, edit the bookmark and replace the URL with the code below and save.
```js
javascript:(function (){location.reload();var i = document.createElement('iframe');document.body.appendChild(i); const tok = i.contentWindow.localStorage.token;prompt("Copy your token below (Clicking OK doesn't copy for you by the way)", tok.replace(/\"/g,""))})()
```
3. Go to https://discord.com/channels/@me and login with your browser and search the name of the bookmark you saved the code on. Click on the bookmark and copy your token.

### Steps on how to use on mobile/Replit
1. Go [here](https://replit.com/signup) to sign up for a Replit account if you don't own one.
2. Navigate to the `Create` tab and click on `+`.
3. Click `Import from GitHub` and enter `
https://github.com/Ewxun/Discord-RPC` into the `GitHub URL` field then click on `+ Import from GitHub`
4. Select `Python` for the language and enter `python3 main.py` for the run command and click `Done`.
5. On mobile, navigate to the `Commands` tab and click on `secrets`. On desktop, click on the padlock icon. Then, enter `TOKEN` at the `key` field and paste your authorization token at the `value` field. Click `Add new secret`
6. Go to [UptimeRobot](https://uptimerobot.com/) and register for an account if you don't have one.
7. Click `+ Monitor`,and enter the following...

|Field|Value|
|:---:|:---:|
|Monitor Type|HTTP(s)|
|Friendly Name|<any name you like\>|
|URL (or IP)|https://<your replit project's name>.<your replit username\>.repl.co<br/>(you can also get the url by setting `replit` to `True` and running the repl once then go to the `Web` tab)|
|Monitoring Interval and Monitoring Timeout|Leave it as it is.|

then click `Create Monitor`.

8. Go back to your repl and modify the config to your needs and you are good to go. (Remember to set `replit` to `True` and do not put your token in [config.yml](config.yml) as people can steal it and log into your Discord account)

To DOs
--
#### Add game connections/checks statuses
- [ ] BrawlStars
- [ ] PUBG
- [x] Minecraft
- [ ] Your ideas

My other projects
--
#### My Discord bot!  
[Invite it]()