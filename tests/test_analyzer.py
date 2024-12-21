---

### Step 6: Add Tests
Write some tests in `tests/test_analyzer.py`:
```python
from resume_analyzer import analyze_resume

def test_analyze_resume():
    sample_text = """
    John Doe
    john.doe@example.com
    +1 123-456-7890
    Skills: Python, Data Analysis
    """
    result = analyze_resume(sample_text)
    assert result["Name"] == "John Doe"
    assert result["Email"] == "john.doe@example.com"
    assert "Python" in result["Skills"]
