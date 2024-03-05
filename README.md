# Discord2Discord

## Auto Forward Discord Message to Discord

![d2d.png](./docs/d2d.png "Discord2Discord")

## Environment

- **Maybe as long as it can run python?**

## How to Start

### Install & Clone

- Install Python
- Install dependencies
    - Conda: `conda env create -f d2d.yml`
    - Pip: `pip install -r requirements.txt`

### Config

- The configuration file is `{ROOT}/conf.py`
  ```python
  # Discord token [string]
  TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
  # Server id [int]
  SERVER = 000000000000000000
  # From channels [list<int>]
  FROM_CHANNELS = [000000000000000000, 000000000000000000]
  # To channel [int]
  TO_CHANNEL = 000000000000000000
  # whether to show Discord message and log on the terminal [False/True]
  Verbose = False
  ```

    - `token` is the Discord token.
    - `SERVER` is the server ID (can be used as a filter).
    - `FROM_CHANNELS` are the channels where messages are from.
    - `TO_CHANNEL` is the channel where messages are to.
    - `Verbose` whether to show Discord message and log on the terminal.

> Tip: How to get (Discord) token?

```
- Open https://discord.com/ On Chrome
- Press F12
- Switch to Network pannel
- Press Ctrl + E to recording network activity
- Login in
- Search auth/login in the Network pannel
- Click that and then click Response
- Copy token
```

> Tip: How to get Discord server (channel) ID?

```
- Right click the Server (Channel)
- Copy Server ID (Copy Channel ID)
```

### Run

> python d2d.py

#### Shortcut for conda env

- Create a cmd file on desktop named `d2d.cmd`
- Write like the following

  ```
  cmd /k "D:\ProgramData\Anaconda3\Scripts\activate.bat d2d & D: & cd D:\Discord2Discord & python d2d.py"
  ```

- Double click this `d2d.cmd` to start it

### Quit

> Ctrl + C

## Acknowledgements

Thanks to [Discord-S.C.U.M](https://github.com/Merubokkusu/Discord-S.C.U.M)!