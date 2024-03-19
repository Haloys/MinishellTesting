# MinishellTesting - Updated Version

This repository contains an updated version of the MinishellTesting framework originally created by [paulogarithm](https://github.com/paulogarithm). Special thanks to the original author for providing a solid foundation for these tests.

## Updates in This Version

- Additional tests covering new cases.
- Integration with GitHub Actions for automated testing.

## How to get it ?
Clone this repo in your minishell folder by using this command :<br/>
`git clone git@github.com:Haloys/MinishellTesting.git`

You should now have something like this
```
[minishell] $ ls
lib  Makefile  src

[minishell] $ git clone git@github.com:Haloys/MinishellTesting.git
...

[minishell] $ ls
lib  Makefile  MinishellTesting  src
```

## How does it works ?
To run the tests, simply do `./MinishellTesting/run`.

To made your own test, you can configure the **commands.txt**'s file in the **config** folder.<br/>
`./MinishellTesting/config/commands.txt`

## How can i code new tests

### Basics
Basically, your **commands.txt**'s file should look like this :
```
:: This is a comment

>>> Cathegory

> Test 1
Command

> Test 2
Command

>>> End
```

The way the line will be executed is as follow :<br/>
`Command | Terminal`

Terminal is replaced by `tcsh` and `./mysh`.<br/>
Then the result of both function are compared.

After all the tests are passed, you get a resume of all cathegories and an overall one.
```
75%  [===============>    ] Cathegory 1
25%  [=====>              ] Cathegory 2

50%  [==========>         ] Overall
```


### Sub-commands
You can also add sub-commands to your tests.


Basically, it will execute this command after the pipe but before the terminal command :<br/>
`Command | Subcommand Terminal`

To add them in your test, you can use the $ sign followed by a space like this in your **commands.txt**'s file.
```
> Test
$ Subcommand
Command

## Updates in This Version

To automate testing with GitHub Actions, you simply need to copy the `minishell_test.yml` file provided at the root of this repository into the `.github/workflows` directory of your own Minishell project. This allows for automatic testing to be set up with minimal effort.

If the `.github/workflows` directory does not exist in your project, you'll need to create it.

(feel free to customize the `EXECUTABLE` and workflow `name` as needed):

Replace https://github.com/Haloys/MinishellTesting.git with your own fork URL if you've made further customizations.
```
