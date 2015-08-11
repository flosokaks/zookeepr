Zookeepr Installation Instructions
==================================

Setup on tuxfamily
==================

Patch pip like this :

https://github.com/pypa/pip/issues/3017

    export PYTHONPATH=/home/kansaslf/kansaslinuxfest.tuxfamily.org-web/php-include/install//lib/python2.7/site-packages/

Remove the old ~/.local

    rm ~/.local/

symlink in the target dir into .local because pip does not change all locations

    ln -s /home/kansaslf/kansaslinuxfest.tuxfamily.org-web/php-include/install ~/.local
  
create a temp dir:

    mkdir -p /home/kansaslf/kansaslinuxfest.tuxfamily.org-web/php-include/install/tmp
  
run pip:

    ~/kansaslf/kansaslinuxfest.tuxfamily.org-web/php-include/install/bin/pip install  -r requirements.txt  --no-cache-dir --user


External dependencies
---------------------

 * libpq-dev
 * libpython-dev
 * libxslt1-dev
 * libxml2-dev
 * postgresql
 * python-virtualenv

I have upgraded to : https://github.com/Pylons/pylons and
https://github.com/Pylons/webob

```
git clone git@github.com:flosokaks/zookeepr.git
cd zookeepr/
sudo apt-get install python-elementtidy
pip install --user --upgrade WebOb, pyramid, pyramid-debugtoolbar, pyramid-tm, transaction, waitress, zope.sqlalchemy, pylibravatar, pylons, repoze.lru, translationstring, zope.deprecation, venusian, pyramid-mako, WebHelpers, WebError, WebTest
pip install --user --upgrade WebOb pyramid pyramid-debugtoolbar pyramid-tm transaction waitress zope.sqlalchemy pylibravatar pylons repoze.lru translationstring zope.deprecation venusian pyramid-mako WebHelpers WebError WebTest
sudo apt-get install python-authkit
git clone git@github.com:Pylons/webob.git
cd webob/ &&  python setup.py install --user
git clone git@github.com:Pylons/pylons.git
cd pylons/ &&  2008  python setup.py install --user
sudo apt-get install libpq-dev libpython-dev libxslt1-dev libxml2-dev
postgresql python-virtualenv


sudo apt-get install postgresql-9.4


as postgres: su - postgres

pg_createcluster 9.4 main
pg_ctlcluster 9.4 main start
createuser --no-createdb --no-createrole --no-superuser zookeepr
createdb -O zookeepr zk
psql --command "ALTER USER zookeepr with PASSWORD 'zookeepr'"


cp development.ini.sample development.ini
vi development.ini
```

Change this line :
```
sqlalchemy.url = postgresql://kansaslf_zookeepr:XXXXPASSWORDXXXX@sql/kansaslf_zookeepr
```

```
git cherry-pick daa1702ec4522a991c5f75b17cb27e15375d2631
alembic --config development.ini history
alembic --config development.ini upgrade head
git reset --hard HEAD^

pserve --reload development.ini
```

Creating a development environment
----------------------------------

1. Create a postgresql database for your ZooKeepr instance. The first command creates the database user, the second the database itself, with the zookeepr user as the admin user, and the third assigns a password to the zookeepr user.

    ```
    sudo -u postgres createuser --no-createdb --no-createrole --no-superuser zookeepr
    sudo -u postgres createdb -O zookeepr zk
    sudo -u postgres psql --command "ALTER USER zookeepr with PASSWORD 'zookeepr'"
    ```

2. Create a virtualenv for your ZooKeepr instance.
        ```
        \# using only virtualenv
        virtualenv env --no-site-packages
        . ./env/bin/activate

        \# using virtualenwrapper
        mkvirtualenv zookeepr # --no-site-packages is default
        workon zookeepr
        ```

3. Configure the virtual environment.

        ```
        cp zkpylons/config/klf_info.py.sample zkpylons/config/klf_info.py
        cp development.ini.sample development.ini
        python setup.py develop
        ```

    Edit development.ini to set sqlachemy.url to match your postgresql database.
    _Note: You must set sqlachemy.url in both the [app:main] and [alembic] sections_

4. Now we populate the database. Run alembic to create and populate the initial database.
        ```
        alembic --config development.ini upgrade head
        ```

        WARNING: On a vanilla trunk this does not currently work but there
        is a workaround:

            * Zookeepr is using alembic in a rather unusual way, which leads to
            problems. James has a work-around for this, but it is not currently in
            master and should never be committed to master. The work-around can be
            cherry-picked, commit daa1702ec4522a991c5f75b17cb27e15375d2631 from
            the nasty-db-import-fix branch.

            ```
            git cherry-pick daa1702ec4522a991c5f75b17cb27e15375d2631
            alembic --config development.ini upgrade head
            ```

            To verify the fix, use the alembic history command and check that the
            head revision is "This revision is a lie and should always be head".
            `alembic --config development.ini history`

            ```
            git reset --hard HEAD^
            ```

            Now, we verify that the revision is no longer present, using the command;
            `alembic --config development.ini history`

            The phrase 'This revision is a lie' should *no longer* be present.

5. Run the development server.
        ```
        pserve --reload development.ini
        ```

6. The default admin account is:
        ```
        email: admin@zookeepr.org
        password: password
        ```

You should now have a development instance of ZooKeepr up and running.

Access it at: <http://0.0.0.0:6543>

*Congratulations*



