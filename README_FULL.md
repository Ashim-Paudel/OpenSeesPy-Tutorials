# OpenSees Learning Resources

## Introduction

Welcome! This repository is designed to help **beginners and researchers** become familiar with **OpenSees** (Open System for Earthquake Engineering Simulation) using Python. 

OpenSees is a powerful, open-source simulation framework for earthquake engineering. However, comprehensive beginner-friendly tutorials are limited in the community. This repository fills that gap by providing well-documented, practical examples that demonstrate core concepts from first principles to advanced applications.

**Target Audience:**
- Students new to structural dynamics and earthquake engineering
- Researchers exploring nonlinear analysis techniques
- Engineers transitioning from commercial software to OpenSees
- Practitioners needing reference implementations for common structural analysis tasks

---

## 📚 Repository Contents

### 1. **Structural Dynamics Fundamentals** 
   📁 `00 A.K Chopra - Structural Dynamics Examples`
   
   Foundational concepts based on A.K. Chopra's textbook:
   - **Sinusoidal Force to SDOF Model** - Single-degree-of-freedom systems under harmonic loading
   - **SDOF Response to Ground Motion** - Time-history response analysis with earthquake records
   - **Response Spectra Concept** - Seismic response spectra generation and interpretation

### 2. **Basic Analysis Types**
   
   **📁 01 Basic Truss Analysis**
   - Elastic truss analysis with linear elements
   - Support reactions and member force calculations
   - Foundation for understanding element formulation

   **📁 02 Fiber Section of RCC Section**
   - Reinforced concrete fiber discretization techniques
   - Visualization of RC cross-sections with reinforcement
   - Introduction to distributed plasticity concepts
   - Functions: `BuildRCrectSection()` - automate RC section creation with custom reinforcement patterns

   **📁 03 Moment Curvature Analysis**
   - Material constitutive relationship verification
   - Section analysis for flexural capacity
   - Utility: `MomentCurvature.py` - automated moment-curvature analysis framework

   **📁 04 Eigen Analysis of 2D Framed Building**
   - Modal analysis of multi-story frame structures
   - Natural frequencies and mode shapes
   - Multiple examples: 2-bay, 3-story, and 5-story buildings
   - Foundation for dynamic analysis setup

### 3. **Cantilever Column Analysis**
   
   **📁 05 Analysis of a 2D Elastic Cantilever Column**
   - Gravity load analysis on elastic cantilever
   - Time-history analysis with earthquake records
   - Visualization of displacements and responses
   - Utility: `Canti2DEQ.py` - cantilever earthquake motion analysis

   **📁 06 Analysis of a 2D Nonlinear Cantilever Column - Uniaxial Inelastic Section**
   - Introduction to material nonlinearity
   - Uniaxial inelastic material models
   - Comparison of elastic vs. nonlinear response
   - Demonstrates effects of yielding and damping

### 4. **Portal Frame Analysis**
   📁 `07 Portal Frame Analysis`
   
   Comprehensive portal frame examples with multiple section types:
   - **Elastic Section Analysis** - Linear behavior reference model
   - **Nonlinear Material Analysis** - Uniaxial inelastic constitutive laws
   - **Fiber Section Analysis** - Distributed plasticity with fiber discretization
   - Demonstrates transition from simple to complex modeling approaches

### 5. **Pushover Analysis**
   
   **📁 08 Monotonic Pushovers**
   - Static nonlinear pushover analysis procedure
   - Utility functions: `model_functions.py`, `analysis_functions.py`, `output_functions.py`
   - Automated load control and analysis loops
   - Capacity curve generation

   **📁 09 Reverse Cyclic Pushover Analysis**
   - Cyclic loading patterns simulating earthquake behavior
   - Utility: `displacement_analysis.py` - cyclic response tracking
   - Hysteretic behavior observation
   - Load reversal handling in analysis

### 6. **Multi-Story Building Models**
   📁 `10 2 Storey Frame`
   
   Complete analysis suite for a 2-story building:
   - **Gravity Analysis** - Dead load and self-weight effects
   - **Modal (Eigen) Analysis** - Dynamic characteristics
   - **Pushover Analysis** - Capacity and demand evaluation
   - **Ground Motion (GMPT) Analysis** - Time-history under seismic motion
   - Demonstrates complete workflow from model creation to seismic response

### 7. **Helper Functions & Utilities**
   📁 `11 Opensees Building Automate Helper Function`
   
   **Purpose:** Automate repetitive modeling tasks and reduce code complexity
   
   **Key Modules:**
   
   - **`modelUnits.py`**
     - Unit conversion utilities (SI, Imperial, mixed systems)
     - Converts: meters, cm, mm, inches, feet, kN, kips, ksi, psi, etc.
     - Simplifies multi-unit modeling workflows
   
   - **`modelFunctions.py`**
     - `getModel(buildingID, NBay, NStory, LBeam, LCol, sectionType, startCoor)`
       - Automated building generation with customizable geometry
       - Section types: Elastic, InElastic, RCFiber, SteelFiber
       - Dynamic node and element tagging system
     - `runGravityAnalysis(steps)` - Execute dead load analysis
     - `setRayleighDamping()` - Configure mass and stiffness proportional damping
     - `runGroundMotionAnalysis(groundMotionData, GM_fact, dt)` - Transient analysis driver
     - Material and section definition helpers
   
   - **`buildFiberSection.py`**
     - `BuildRCrectSection()` - Create RC fiber sections with reinforcement
       - Confined core and unconfined cover patches
       - Multiple steel reinforcement layers (top, bottom, intermediate)
       - Customizable fiber discretization
       - Built-in cross-section visualization
     - `BuildSteelWSection()` - Generate steel W-section fiber models
       - Automatic web and flange discretization
       - Parametric section definition
   
   - **`example.py`**
     - Complete workflow demonstration
     - Building creation → Gravity analysis → Dynamic analysis → Time-history response
     - Shows integration of all utilities

### 8. **Theoretical Foundations**
   📁 `Theories in Opensees`
   
   **Materials Elements and Geometric Transformations**
   - Detailed explanations of material constitutive models
   - Element formulations and assumptions
   - Geometric transformation types and P-Delta effects
   - Theoretical background for advanced modeling

---

## 🎓 Basics Covered

| Topic | Status | Location |
|-------|--------|----------|
| OpenSees fundamentals | ✅ | Examples 00-01 |
| Linear elastic analysis | ✅ | 01, 04, 07 |
| Fiber section modeling | ✅ | 02, 07, 11 |
| Moment-curvature analysis | ✅ | 03 |
| Gravity load analysis | ✅ | 05, 10 |
| Modal/Eigen analysis | ✅ | 04, 10 |
| Time-history analysis | ✅ | 00, 05, 10 |
| Pushover analysis (static) | ✅ | 08, 10 |
| Cyclic analysis | ✅ | 09 |
| Nonlinear material models | ✅ | 06, 07, 10 |
| P-Delta effects | ✅ | 07-10, Helper functions |
| Damping formulations | ✅ | 10, Helper functions |
| Building automation | ✅ | 11 |

---

## 💡 Why This Repository Helps Beginners

✅ **Documented from first principles** - Even the most basic concepts are explained
✅ **Jupyter Notebooks** - Interactive code with markdown explanations
✅ **Rich visualizations** - Structural models, mode shapes, hysteresis plots, response spectra
✅ **Progressive complexity** - Start simple, advance to nonlinear multi-story buildings
✅ **Reusable utilities** - Reduces boilerplate for common tasks
✅ **Real earthquake records** - Examples use actual seismic data files
✅ **Beginner-written** - Author learned OpenSees from scratch (Apr 2024), understands beginner perspective

---

## ⚠️ Important Notes

### Scope & Limitations
- **2D Models Only** - Examples are currently limited to 2D structural analysis (XY plane)
- **Educational Focus** - Models emphasize understanding over production optimization
- **Use at Your Own Risk** - Some analyses may contain approximations; verify results independently
- **No Professional Review** - This is a learning resource, not a professional design tool

### Before Using in Research/Professional Work:
1. Verify model assumptions against your analysis requirements
2. Check material properties and element formulations
3. Validate against known benchmarks or hand calculations
4. Consult OpenSees documentation and published literature
5. Have work reviewed by qualified structural engineers

---

## 🚀 Getting Started

### Prerequisites
```
Python 3.6+
openseespy
matplotlib
numpy
jupyter (for Jupyter Notebooks)
opsvis (for structural visualization)
```

### Installation
```bash
# Install OpenSees Python bindings
pip install openseespy

# Install visualization dependencies
pip install opsvis matplotlib numpy

# Install Jupyter (optional, for interactive notebooks)
pip install jupyter
```

### Quick Start
1. Open any Jupyter notebook in the repository
2. Read the markdown explanations
3. Run code cells and observe results
4. Modify parameters to experiment

### Example: Using Helper Functions
```python
from modelUnits import *
from modelFunctions import *
from buildFiberSection import *
import openseespy.opensees as ops

# Remove old model
ops.wipe()
ops.model('BasicBuilder', '-ndm', 2, '-ndf', 3)

# Build a 3-story, 1-bay frame with RC fiber sections
getModel(buildingID=10, NBay=1, NStory=3, LBeam=4*m, LCol=4*m, 
         sectionType='RCFiber', startCoor=(0, 0))

# Run gravity analysis
runGravityAnalysis(100)

# Run earthquake analysis
setRayleighDamping()
# ... load earthquake data and run analysis
```

---

## 📖 References & Learning Resources

### OpenSees Documentation
- [OpenSees Official Wiki](https://opensees.berkeley.edu/wiki/index.php?title=Command_Manual)
- [OpenSees Example Manual](https://opensees.berkeley.edu/wiki/index.php/Examples)
- [OpenSeesPy Documentation](https://openseespydoc.readthedocs.io/en/latest/index.html)

### Learning Resources
- [PortWood Digital](https://portwooddigital.com/) - OpenSees tutorials and courses
- [Christian Slotboom's OpenSeesPy Tutorials](https://github.com/cslotboom/OpenSeesPyTutorials) - Video tutorials and code
- A.K. Chopra, *Dynamics of Structures: Theory and Applications* - Foundational textbook referenced in examples

### Structural Dynamics & Earthquake Engineering
- PEER (Pacific Earthquake Engineering Research Center) publications
- Earthquake Records Database (PEER NGA, ESM, etc.)

---

## 📝 Recommended Learning Path

**For Absolute Beginners:**
1. Start with: `00 A.K Chopra Examples` - Understand SDOF dynamics
2. Then: `01 Basic Truss Analysis` - Learn element and node concepts
3. Then: `02 Fiber Section` - Understand section discretization
4. Then: `04 Eigen Analysis` - Multi-degree-of-freedom systems
5. Then: `03 Moment Curvature` - Material nonlinearity

**For Building Analysis:**
1. `04 Eigen Analysis` - Modal properties
2. `07 Portal Frame Analysis` - Structural types progression
3. `10 2 Storey Frame` - Complete workflow
4. `08-09 Pushover/Cyclic Analysis` - Seismic capacity

**For Advanced Topics:**
1. `06 Nonlinear Cantilever` - Nonlinear dynamics
2. `09 Cyclic Pushover` - Hysteresis and energy dissipation
3. `Theories in OpenSees` - Theoretical foundations
4. `11 Helper Functions` - Optimization and automation

---

## 🎯 How to Use This Repository

### Learning
- Use as a tutorial resource for OpenSees concepts
- Modify examples to experiment with different parameters
- Run analyses to build intuition about structural behavior

### Research
- Adapt examples for your research models
- Use helper functions as starting templates
- Reference for methodology and analysis procedures

### Teaching
- Use examples in classroom demonstrations
- Assign examples as learning exercises
- Modify for specific course objectives

---

## 🔄 Contributing Improvements

Found an error or have improvements? This is a learning repository—feedback helps:
- Report issues or inconsistencies
- Suggest clearer explanations
- Share additional examples
- Report bugs in helper functions

---

## 📋 File Structure

```
OpenSees Learning/
├── 00 A.K Chopra - Structural Dynamics Examples/
│   ├── Sinusoidal Force to SDOF Model.ipynb
│   ├── SDOF Response Ground Motion.ipynb
│   └── Response Spectra Concept.ipynb
├── 01 Basic Truss Analysis/
├── 02 Fiber Section of RCC section/
├── 03 Moment Curvature Analysis/
├── 04 Eigen Analysis of 2d framed building/
├── 05 Analysis of a 2D Elastic Cantilever Column/
├── 06 Analysis of a 2D Nonlinear Cantilever Column/
├── 07 Portal Frame Analysis/
├── 08 Monotonic Pushovers/
├── 09 Reverse Cyclic Pushover Analysis/
├── 10 2 Storey Frame/
├── 11 Opensees Building Automate Helper Function/
│   ├── modelUnits.py         # Unit conversions
│   ├── modelFunctions.py     # Automation utilities
│   ├── buildFiberSection.py  # Section builders
│   ├── example.py            # Integration example
│   └── data/                 # Earthquake records
├── Theories in Opensees/
└── README_FULL.md           # This file
```

---

## 📄 License

This repository is licensed under the **MIT License**. See [LICENSE](LICENSE) file for details.

**Summary:** You are free to use, modify, and distribute this code for personal, educational, and research purposes.

---

## 🙏 Citation

If you use code or examples from this repository in your research, publications, or projects, **please cite this work**:

### BibTeX
```bibtex
@misc{paudel2024openseeslearning,
  title={OpenSees Learning Resources: Python Examples for Structural Dynamics and Earthquake Engineering},
  author={Paudel, Ashim},
  year={2024},
  publisher={GitHub},
  howpublished={\url{https://github.com/Ashim-Paudel/OpenSees_Learning}}
}
```

### APA Format
```
Paudel, A. (2024). OpenSees Learning Resources: Python examples for structural dynamics 
and earthquake engineering [Computer software]. Retrieved from 
https://github.com/Ashim-Paudel/OpenSees_Learning
```

### Chicago Format
```
Paudel, Ashim. OpenSees Learning Resources: Python Examples for Structural Dynamics 
and Earthquake Engineering. Computer software. Accessed [date]. 
https://github.com/Ashim-Paudel/OpenSees_Learning.
```

### Simple Text Citation
```
Paudel, A. (2024). OpenSees Learning Resources. GitHub Repository. 
https://github.com/Ashim-Paudel/OpenSees_Learning
```

### For Code Snippets or Functions
```
"Adapted from Paudel (2024) OpenSees Learning Resources, specifically the 
[module/example name]. Retrieved from 
https://github.com/Ashim-Paudel/OpenSees_Learning"
```

---

## 👤 Author

**Ashim Paudel**  
- Started learning OpenSees: April 2024
- Created this repository to help others on the same learning journey
- Repository combines practical examples with theoretical foundations

---

## 🎓 Acknowledgments

This learning repository builds on:
- **OpenSees** - PEER/UC Berkeley
- **A.K. Chopra** - Foundational textbook on Structural Dynamics
- **OpenSeesPy Community** - Python bindings and documentation
- **PortWood Digital** - Excellent OpenSees tutorials
- **Christian Slotboom** - OpenSeesPy tutorial videos

---

## 📧 Questions & Support

For questions about:
- **OpenSees usage** - Refer to [OpenSees Wiki](https://opensees.berkeley.edu/wiki/)
- **This repository** - Check relevant notebook or helper function documentation
- **General concepts** - Review theory sections or reference materials

---

## 📅 Version History

- **v1.0** (2024) - Initial release with 11 example modules and helper utilities

---

**Last Updated:** 2024  
**Status:** Active Learning Repository

