# Introduction

This is the source code for the sample app that was used during the code lab at GDG Kuwait's weekly session
on Feb 11, 2015.

# How to use the code

1. Sign up for a [Google Cloud Account](https://console.developers.google.com/start/appengine) (its free!)
2. Install the [Google App Engine SDK for Python](https://cloud.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python)
3. Create a [project](https://console.developers.google.com/?getstarted=https://appengine.google.com)
4. Authenitcate yourself to Google cloud, by running `gcloud auth login` at your terminal (you only need to do this once).
5. If there are any component updates, you can install them with `gcloud components update`

Note down the name of your project, which you'll need later on.

You will also need a sample resource file `resource.cgn`, which you can obtain from your bank. Place this file
in the same location as `main.py`.

To deploy the application:

1. Clone the repository
2. Update the `app.yaml` file and replace `gdg-knet` with the name of your project.
3. Edit `main.py` and replace `ALIAS = 'aub'` with the alias for your terminal.
4. Upload the project by typing `appcfg.py update /path/to/the/repository`

For more information on the transaction process,
see the [documentation for `e24PaymentPipe`](https://e24paymentpipe.readthedocs.org)
