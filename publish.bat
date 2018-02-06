REM Atualiza o repositório no Github e publica o pacote o PyPi
REM Argumentos:
REM   * "mensagem de commit"
REM   * número da versão

echo OFF

echo - Atualizando versão para %2
echo __version__ = '%2' > .\sgs\__version__.py

echo - Atualizando repositório do Github
git add .
git commit -m %1
git tag %2
git push
git push --tags

echo - Realizando upload para o Pypi
python setup.py sdist upload -r pypi
