import subprocess
from typing import Dict


def _freeze_to_dict(string: str):
    for line in string.splitlines():
        line = line.split('==')
        if len(line) == 1:
            yield line[0], ""
        else:
            yield line[0], line[1]


def freeze_to_dict(string: str):
    return dict(_freeze_to_dict(string))


def get_installed_version():
    """
    pip freeze
    를 이용해 설치된 package 목록을 가져온다.
    """
    freeze = subprocess.Popen(
        args=['pip', 'freeze'],
        stdout=subprocess.PIPE
    )
    out, err = freeze.communicate()
    return freeze_to_dict(out.decode())


def check_version(requirement: str, package: Dict[str, str]):
    """
    `requirement`파일의 내용을 설치되어있는 패키지로 업데이트 한다.
    """
    with open(requirement) as f_in:
        requirement_package = freeze_to_dict(f_in.read())

    print(requirement)
    for p, v in requirement_package.items():
        if v != package[p]:
            print(p, v, '=>', package[p])
    print()

    with open(requirement, 'w') as f_out:
        for p, v in requirement_package.items():
            print(p, package[p], sep="==", file=f_out)


def main():
    package = get_installed_version()
    check_version('requirements.txt', package)
    check_version('requirements-dev.txt', package)


if __name__ == '__main__':
    main()
