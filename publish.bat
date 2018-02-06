echo OFF
echo Publicando versao %2 do pacote
echo ==============================
echo __version__ = '%2' > .\sgs\__version__.py
git add .
git commit -m %1
git tag %2
git push
git push --tags
python setup.py sdist upload -r pypi
