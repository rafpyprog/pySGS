echo 'Publicando versão %2 do pacote'
echo '=============================='
echo __version__ = '%2' > .\sgs\__version__.py
git add .
git commit -m "%1"
git tag %2
git push
git push --tags
echo python setup.py sdist upload -r pypi
