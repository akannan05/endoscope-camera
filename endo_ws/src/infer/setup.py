from setuptools import find_packages, setup
import os
import glob

package_name = 'infer'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'ultralytics', 'rosnumpy', 'rclpy'],
    zip_safe=True,
    maintainer='akannan05',
    maintainer_email='akannan05@g.ucla.edu',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'detector=infer.polyp_inference:main',
        ],
    },
)
