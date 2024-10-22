# Activate virtual environment
source env/Scripts/activate

# Set encoding
export PYTHONIOENCODING=utf-8
echo "Encoding set to $PYTHONIOENCODING"

# Install requirements
pip install -r requirements.txt
echo "Requirements installed"
