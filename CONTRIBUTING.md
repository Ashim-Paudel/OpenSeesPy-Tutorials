# Contributing & Attribution Guide

Thank you for your interest in improving the OpenSees Learning Resources! This guide explains how to contribute, what we're looking for, and how to properly attribute work.

---

## 🤝 Types of Contributions Welcome

We appreciate contributions that help make this a better learning resource:

### **Documentation Improvements**
- Fix typos, grammar, or unclear explanations
- Enhance existing examples with better comments
- Improve README and guide clarity
- Add learning path recommendations

### **Code Enhancements**
- Bug fixes in Python helper functions
- Improved visualization outputs
- More efficient implementations
- Additional helper functions that automate common tasks

### **New Examples**
- Additional analysis types (3D models, dampers, isolation systems)
- New material models or element types
- Additional real-world case studies
- Comparison of different modeling approaches

### **Educational Content**
- Additional theory explanations
- Worked-out example problems
- Quick reference guides
- FAQ sections for common issues

### **Testing & Validation**
- Verify examples work with latest OpenSees versions
- Compare results against published benchmarks
- Document limitations or edge cases
- Identify inconsistencies

### **Community Help**
- Answer questions in issues
- Share your own learning experiences
- Suggest improvements based on your use
- Help other beginners

---

## 📋 Contributing Process

### **Before You Start**
1. Read this guide completely
2. Check the LICENSE and understand terms
3. Review existing examples to understand style
4. Consider opening an Issue to discuss major changes

### **For Small Changes** (Typos, minor fixes)
1. Fork the repository
2. Create a new branch: `fix/descriptive-name`
3. Make your changes
4. Commit with a clear message (see Commit Guidelines below)
5. Push and create a Pull Request

### **For Major Contributions** (New examples, significant refactoring)
1. Open an Issue first to discuss your proposal
2. Get feedback from maintainers
3. Fork the repository
4. Create a new branch: `feature/descriptive-name`
5. Implement your contribution with tests/examples
6. Document thoroughly
7. Submit Pull Request with detailed description

### **For Bug Reports**
1. Open an Issue with:
   - Clear title describing the problem
   - Steps to reproduce
   - Expected vs. actual behavior
   - Your environment (Python version, OpenSees version)
   - Relevant error messages or screenshots

---

## ✍️ Commit Guidelines

### Commit Message Format
```
Type: Brief description (50 chars max)

More detailed explanation if needed (wrap at 72 chars).
Explain what was changed and why.

Resolves #123 (if applicable)
```

### Commit Types
- `docs:` - Documentation changes
- `fix:` - Bug fixes
- `feat:` - New features or examples
- `refactor:` - Code restructuring without changing behavior
- `test:` - Adding or updating tests/validation
- `style:` - Code style improvements (formatting, naming)
- `chore:` - Build process, dependencies, tooling

### Examples
```
fix: Correct moment curvature calculation in nonlinear analysis

The moment calculation was using incorrect section properties
when multiple fiber layers were present. Fixed by properly
summing across all fibers.

docs: Add learning path recommendations to README

Added recommended study sequence for beginners and researchers,
with links to relevant examples.

feat: Add 3D portal frame analysis example

New example demonstrating 3D building analysis including
torsional effects and 3D earthquake ground motions.
```

---

## 📝 Code Style & Standards

### Python Code Style
- Follow PEP 8 conventions
- Use meaningful variable names
- Add docstrings to functions explaining purpose and parameters
- Keep functions focused and modular
- Add comments for non-obvious logic

### Example Function Documentation
```python
def BuildRCrectSection(id, HSec, BSec, coverH, coverB, 
                      coreID, coverID, steelID, 
                      numBarsTop, barAreaTop, numBarsBot, barAreaBot, 
                      numBarsIntTot, barAreaInt, 
                      nfCoreY, nfCoreZ, nfCoverY, nfCoverZ, 
                      plotFibSec=True):
    """
    Build fiber rectangular RC section with confined core.
    
    Automated creation of reinforced concrete fiber sections with:
    - Confined concrete core
    - Unconfined cover patches
    - Multiple reinforcement layers
    
    Parameters
    ----------
    id : int
        Unique section identifier
    HSec : float
        Section depth (height) along local-y axis
    BSec : float
        Section width along local-z axis
    coverH : float
        Depth of cover concrete (distance to reinforcement NA)
    coverB : float
        Width of cover concrete
    coreID : int
        Material tag for confined core concrete
    coverID : int
        Material tag for unconfined cover concrete
    steelID : int
        Material tag for reinforcing steel
    numBarsTop : int
        Number of bars in top layer
    [... more parameters ...]
    plotFibSec : bool, optional
        Whether to plot the fiber section visualization (default: True)
    
    Returns
    -------
    None
        Creates fiber section in OpenSees model
    
    Notes
    -----
    Section coordinates centered at (0, 0) in local axes.
    Core concrete boundary defined by reinforcement cover distance.
    
    Examples
    --------
    >>> BuildRCrectSection(
    ...     id=1, HSec=24, BSec=24, coverH=2, coverB=2,
    ...     coreID=1, coverID=2, steelID=3,
    ...     numBarsTop=4, barAreaTop=2.0, numBarsBot=4, barAreaBot=2.0,
    ...     numBarsIntTot=4, barAreaInt=1.0,
    ...     nfCoreY=10, nfCoreZ=10, nfCoverY=5, nfCoverZ=5
    ... )
    """
    # Implementation...
```

### Jupyter Notebook Style
- Use markdown cells for explanations before code
- Break complex analyses into logical sections
- Include comments for non-obvious steps
- Provide context for each analysis section
- Add section headers with markdown

### Documentation
- Write in clear, beginner-friendly language
- Explain concepts before presenting code
- Include diagrams or visualizations where helpful
- Link to relevant OpenSees documentation
- Define technical terms on first use

---

## 🏷️ Attribution & Licensing

### Your Rights
- Your contributions will be licensed under MIT License
- You retain copyright to your contributions
- Your work can be used commercially with attribution
- Your work may be modified by others (with attribution)

### Proper Attribution
When contributing, ensure:
1. **Copyright notice** - Include your name and contribution year
2. **License compatibility** - Your code must be compatible with MIT
3. **Third-party code** - Only include code you have rights to use
4. **Attribution for borrowed code** - Always credit the original source

### Example Attribution in Code
```python
# BuildRCrectSection - Fiber section builder for RC columns
# Based on methodology by Silvia Mazzoni (2006) and Michael H. Scott (2003)
# Adapted and extended by Ashim Paudel (2024)
# Further improvements by [Your Name] (2024)
# Licensed under MIT License
```

### For Significant Contributions
If your contribution is substantial:
1. Add your name to a CONTRIBUTORS file (we'll create this)
2. Include your contribution type and area
3. Optional: Add your GitHub profile link

---

## 📚 Documentation Standards

### README Updates
When adding new examples, update README with:
- Brief description of what's covered
- What concepts are demonstrated
- Who should study this section
- Key utilities or functions used
- Link to the specific notebook or file

### Example Documentation
```markdown
**📁 12 Advanced 3D Analysis** (new example)

Comprehensive examples for 3D structural analysis:
- 3D building model creation
- P-Delta effects in 3D space
- Torsional dynamics
- 3D earthquake ground motions
- Comparison of 2D vs. 3D modeling approaches

**Best for:** Researchers, advanced practitioners  
**Prerequisites:** Understanding of 2D analysis (Examples 01-10)  
**Key utilities:** getModel3D(), applyMultipleSupport3D()
```

---

## 🧪 Testing & Validation

### Before Submitting
1. **Run all notebooks** to ensure they execute without errors
2. **Verify visualizations** appear correctly
3. **Check calculations** against known results or benchmarks
4. **Test on different systems** if possible
5. **Document any dependencies** (versions, packages)

### For New Examples
1. Include verification against hand calculations
2. Compare with published results if available
3. Document any approximations or assumptions
4. Note performance characteristics (runtime, memory)

### For Bug Fixes
1. Include a test case demonstrating the bug
2. Verify the fix resolves the issue
3. Check that fix doesn't break other examples
4. Document why the bug occurred

---

## 🚀 Pull Request Process

### PR Title
Clear, descriptive title:
```
Add 3D building analysis example
Fix moment-curvature calculation for composite sections
Improve BuildRCrectSection documentation and add validation
```

### PR Description
Include:
- **What:** What changes are you making?
- **Why:** Why are these changes needed?
- **How:** How do the changes work?
- **Testing:** How did you verify the changes?
- **Issues:** References to related Issues (e.g., "Resolves #42")

### PR Template
```markdown
## Description
Brief description of changes.

## Type of Change
- [ ] Bug fix
- [ ] New feature/example
- [ ] Documentation improvement
- [ ] Code refactoring
- [ ] Performance improvement

## Related Issue
Resolves #(issue number)

## How Has This Been Tested?
Describe testing performed and environment.

## Checklist
- [ ] Code follows PEP 8 style guidelines
- [ ] Documentation updated
- [ ] All examples run without errors
- [ ] Added/updated docstrings
- [ ] No breaking changes to existing code
- [ ] Verified results against known benchmarks

## Additional Context
Any additional information relevant to this PR.
```

---

## 💬 Discussion Guidelines

### Be Respectful
- Assume good intentions
- Be constructive in feedback
- Accept criticism gracefully
- Help others learn

### Ask Good Questions
- Search existing issues first
- Provide context and example code
- Include error messages
- Describe what you've already tried

### Give Useful Feedback
- Be specific, not vague
- Suggest solutions, not just problems
- Acknowledge good work
- Help others improve

---

## ❌ What We Can't Accept

- **Proprietary code** - Must be MIT-compatible
- **Code without attribution** - Always credit sources
- **Examples promoting unsafe practices** - We're educational
- **Unrelated content** - Must align with repository purpose
- **Spam or advertising** - Only genuine contributions
- **Code that violates others' copyrights** - Always respect IP

---

## 🎓 Attribution Examples

### For Modifications to Existing Code
```python
# Original: BuildRCrectSection by Ashim Paudel (2024)
# Based on: Silvia Mazzoni and Michael H. Scott
# Modified by: [Your Name] (2024) to support circular sections
```

### For New Examples
```
# Adaptive Pushover Analysis Example
# Created by: [Your Name] (2024)
# Based on ASCE 41 guidelines
# For: OpenSees Learning Resources
# License: MIT
```

### In Jupyter Notebooks
Add a markdown cell at the beginning:
```markdown
## Author & Attribution

Created by: [Your Name]  
Date: [Date]  
Based on: [Original source/concept]  
Related to: [Existing examples]  

**License:** MIT - See LICENSE file for terms
```

---

## 📖 References for Contributors

### OpenSees Resources
- [OpenSees Wiki](https://opensees.berkeley.edu/wiki/index.php?title=Command_Manual)
- [OpenSeesPy Documentation](https://openseespydoc.readthedocs.io/)

### Python & Code Quality
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [NumPy Docstring Guide](https://numpydoc.readthedocs.io/en/latest/format.html)

### Earthquake Engineering
- [PEER Ground Motion Database](https://ngawest2.berkeley.edu/)
- [A.K. Chopra - Structural Dynamics](https://www.pearson.com/en-us.html) (reference textbook)

---

## ❓ Questions?

Before contributing, you can:
1. Check existing Issues and Discussions
2. Review similar contributions
3. Open an Issue to ask questions
4. Comment on related Pull Requests

---

## 🎉 Thank You!

We truly appreciate your interest in making OpenSees more accessible to beginners and researchers. Your contributions—whether code, documentation, or community support—help advance structural engineering education.

**Every contribution, no matter how small, helps this repository grow!**

---

## 📝 License Reminder

By contributing to this repository, you agree that your contributions will be licensed under the MIT License. You retain copyright to your work, and others may use your contributions with proper attribution.

See [LICENSE](LICENSE) for full details.

