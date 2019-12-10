# *pyzmq* module for Package Control

[![Github Action](https://github.com/packagecontrol/pyzmq/workflows/test/badge.svg)](https://github.com/packagecontrol/pyzmq)


This is the *[pyzmq][]* module
bundled for usage with [Package Control][],
a package manager
for the [Sublime Text][] text editor.


this repo | pypi
---- | ----
![latest tag](https://img.shields.io/github/tag/packagecontrol/pyzmq.svg) | [![pypi](https://img.shields.io/pypi/v/pyzmq.svg)][pypi]

## How to use *pyzmq* as a dependency

In order to tell Package Control
that you are using the *pyzmq* module
in your ST package,
create a `dependencies.json` file
in your package root
with the following contents:

```js
{
   "*": {
      "*": [
         "pyzmq"
      ]
   }
}
```

If the file exists already,
add `"pyzmq"` to the every dependency list.

Then run the **Package Control: Satisfy Dependencies** command
to make Package Control
install the module for you locally
(if you don't have it already).

After all this
you can use `import zmq`
in any of your Python plugins.

See also:
[Documentation on Dependencies](https://packagecontrol.io/docs/dependencies)


## Contributions


The files were built by github [workflows][].

### Personal access token

The secret `${{ secrets.GITHUB_TOKEN }}` does not have the necessary permission
to perform some of the jobs. Please following github instruction to
generate a PAT and put it as secret `GITHUB_PAT`.

### Trigger build manually

The `build` workflow could be triggered by the following request.
```bash
curl -i -H "authorization: Bearer $GITHUB_PAT" \
   -H 'Accept: application/vnd.github.everest-preview+json' \
   -d '{"event_type": "build"}' \
   https://api.github.com/repos/packagecontrol/pyzmq/dispatches
```

## License

The contents of the root folder
in this repository
are released
under the *public domain*.
The contents of all the subfolders
fall under *their own bundled licenses*.



[pyzmq]: https://pypi.org/project/pyzmq/
[Package Control]: https://packagecontrol.io/
[Sublime Text]: https://sublimetext.com/
[pypi]: https://pypi.python.org/pypi/pyzmq
[workflows]: https://github.com/packagecontrol/pyzmq/tree/master/.github/workflows

