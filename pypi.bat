rm build -Recurse
rm dist -Recurse
rm schoolInfo.egg-info

python setup.py sdist bdist_wheel
python -m twine upload dist/*