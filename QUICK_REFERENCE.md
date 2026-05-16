# 🚀 Quick Reference Card - OpenSees Learning Resources

## 📖 Where to Find What

| Need | Look Here | Type |
|------|-----------|------|
| **Learn OpenSees** | README_FULL.md | 📘 Guide |
| **Legal terms** | LICENSE | ⚖️ Legal |
| **Cite this repo** | CITATION.md | 📚 Formats |
| **Contribute code** | CONTRIBUTING.md | 🤝 Guidelines |
| **Full overview** | This card | ⚡ Quick ref |

---

## 📚 Learning Paths

### 🟢 **Beginner Path** (First Time with OpenSees)
1. Example 00 - Structural Dynamics Fundamentals
2. Example 01 - Basic Truss Analysis
3. Example 02 - Fiber Sections
4. Example 04 - Eigen Analysis
5. Example 03 - Moment Curvature

### 🟡 **Intermediate Path** (Multi-Story Buildings)
1. Example 04 - Eigen Analysis (review)
2. Example 07 - Portal Frame Analysis
3. Example 10 - Complete 2-Story Frame
4. Example 08 - Pushover Analysis

### 🔴 **Advanced Path** (Nonlinear Dynamics)
1. Example 06 - Nonlinear Cantilever
2. Example 09 - Cyclic Pushover Analysis
3. Example 10 - Ground Motion Analysis
4. Theories in OpenSees - Deep dive

---

## ✏️ Citation Formats (Copy & Paste Ready)

### **APA** - For most academic papers
```
Paudel, A. (2024). OpenSees learning resources: Python examples for structural 
dynamics and earthquake engineering [Computer software]. GitHub. 
https://github.com/Ashim-Paudel/OpenSees_Learning
```

### **BibTeX** - For LaTeX documents
```bibtex
@misc{paudel2024openseeslearning,
  author = {Paudel, Ashim},
  title = {OpenSees Learning Resources: {P}ython Examples for Structural 
           Dynamics and Earthquake Engineering},
  year = {2024},
  howpublished = {GitHub Repository},
  url = {https://github.com/Ashim-Paudel/OpenSees_Learning}
}
```

### **Chicago** - Humanities/historical style
```
Paudel, Ashim. "OpenSees Learning Resources: Python Examples for Structural 
Dynamics and Earthquake Engineering." GitHub Repository. Accessed [date]. 
https://github.com/Ashim-Paudel/OpenSees_Learning.
```

### **Simple Text** - Any format
```
Paudel, A. (2024). OpenSees Learning Resources. Retrieved from 
https://github.com/Ashim-Paudel/OpenSees_Learning
```

---

## 📋 Helper Functions Quick Guide

### **In Folder: `11 Opensees Building Automate Helper Function`**

**Module: modelUnits.py**
- Unit conversions (SI, Imperial, mixed)
- Convert: m, cm, mm, ft, inch, kN, kips, ksi, psi, etc.

**Module: modelFunctions.py**
- `getModel()` - Create building automatically
- `runGravityAnalysis()` - Gravity load analysis
- `setRayleighDamping()` - Configure damping
- `runGroundMotionAnalysis()` - Earthquake analysis

**Module: buildFiberSection.py**
- `BuildRCrectSection()` - RC fiber sections with reinforcement
- `BuildSteelWSection()` - Steel W-section fiber models

**Module: example.py**
- Complete workflow demonstration
- Shows integration of all utilities

---

## ⚙️ Key Info at a Glance

| Property | Value |
|----------|-------|
| **Author** | Ashim Paudel |
| **Year** | 2024 |
| **License** | MIT |
| **Repository** | https://github.com/Ashim-Paudel/OpenSees_Learning |
| **Language** | Python |
| **Format** | Jupyter Notebooks + Python scripts |
| **Main Tool** | OpenSees (openseespy) |

---

## 🚀 Installation

```bash
# Install dependencies
pip install openseespy opsvis matplotlib numpy jupyter

# Clone repository
git clone https://github.com/Ashim-Paudel/OpenSees_Learning.git
cd "OpenSees Learning"

# Open notebooks
jupyter notebook
```

---

## ❓ Common Questions

### **Q: Can I use this for my research paper?**
✅ **Yes!** Just cite it using formats from CITATION.md

### **Q: Can I modify the code?**
✅ **Yes!** MIT License allows modifications. Must provide attribution.

### **Q: Can I use this commercially?**
✅ **Yes!** Must cite and provide license notice.

### **Q: Can I teach this?**
✅ **Yes!** Great for classroom use. Cite appropriately.

### **Q: Is this suitable for professional design?**
⚠️ **No.** Educational resource. Have professional engineer review.

### **Q: How do I cite a specific example?**
See CITATION.md for "Citing by Use Case" section.

### **Q: How do I contribute?**
Read CONTRIBUTING.md - follow the process there.

---

## 📝 Files at a Glance

```
OpenSees Learning/
├── README_FULL.md          ← START HERE (main guide)
├── LICENSE                 ← Read before using commercially
├── CITATION.md             ← How to cite (multiple formats)
├── CITATION.cff            ← GitHub automatic citation
├── CONTRIBUTING.md         ← How to contribute/improve
├── SETUP_SUMMARY.md        ← This setup was documented here
├── 00-11 Examples/         ← Learning materials
└── README.md               ← Original brief overview
```

---

## 🔗 Important Links

- **OpenSees Official:** https://opensees.berkeley.edu/
- **OpenSeesPy Docs:** https://openseespydoc.readthedocs.io/
- **Repository:** https://github.com/Ashim-Paudel/OpenSees_Learning
- **License:** MIT (see LICENSE file)

---

## ⚠️ Important Disclaimers

- ⚠️ **Educational Only** - Not for professional design use
- ⚠️ **Use at Own Risk** - Verify results independently
- ⚠️ **2D Models Only** - Current examples are 2D
- ⚠️ **Beginner Focus** - May contain simplifications

---

## ✅ Quick Checklist

**Using this repository?**
- [ ] Read README_FULL.md
- [ ] Understand LICENSE terms
- [ ] Cite appropriately in your work
- [ ] Verify results for your application

**Contributing improvements?**
- [ ] Read CONTRIBUTING.md
- [ ] Follow code style guidelines
- [ ] Include proper attribution
- [ ] Write clear commit messages

**Publishing research?**
- [ ] Choose citation format from CITATION.md
- [ ] Add to references section
- [ ] Include in acknowledgments
- [ ] Add in-text citations

---

## 🆘 Need Help?

| Issue | Solution |
|-------|----------|
| OpenSees question | https://opensees.berkeley.edu/wiki/ |
| Python error | Check Python docs |
| How to cite | See CITATION.md |
| Bug report | Open GitHub issue |
| Contribution idea | Read CONTRIBUTING.md |

---

## 🎓 Attribution Examples

**In a paper:**
```
"The modeling approach follows Paudel (2024), using the OpenSees Learning 
Resources for fiber section discretization and ground motion analysis."
```

**In code:**
```python
# Based on OpenSees Learning Resources (Paudel, 2024)
# https://github.com/Ashim-Paudel/OpenSees_Learning
```

**In thesis/dissertation:**
```
"The analysis framework presented here is based on the OpenSees Learning 
Resources (Paudel, 2024), which provides comprehensive examples for structural 
dynamics analysis using Python."
```

---

## 📞 Contact & Support

- **For OpenSees issues:** Use official OpenSees forums
- **For Python issues:** Python documentation
- **For this repository:** Check GitHub issues
- **For citations:** See CITATION.md

---

**Version:** 1.0  
**Last Updated:** 2024  
**License:** MIT  

**Happy Learning! 🚀**

