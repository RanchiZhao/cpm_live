from setuptools import setup, find_packages

def main():
    setup(
        name='cpm_live',
        version='0.1.2',
        description="cpm_live series",
        author="OpenBMB",
        author_email="ranchizhao@gmail.com",
        packages=find_packages(exclude='cpm_live'),
        url="https://github.com/OpenBMB/BMCook",
        license="Apache 2.0"
    )

if __name__ == "__main__":
    main()