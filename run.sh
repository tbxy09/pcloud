cp app.py build
cp -rd cloud_api build
cp -rd util build
mkdir build/templates
sudo chown -R tbxy09:tbxy09  build/templates
cp templates/hello.html build/hello.html
cp -rd themes/rating build/static/css
ln -sf ../hello.html build/templates/hello.html
cp node_modules/jquery-bar-rating/dist/jquery.barrating.min.js build/static/js/
ln -sf ../index.html build/templates/index.html
python build/app.py
