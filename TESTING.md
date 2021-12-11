# [Sportsporium](https://rs87801-sportsporium.herokuapp.com/)

## Table of contents

-  [Testing](#testing)
    - [Testing User Stories](#testing-user-stories)
    - [Manual Testing](#manual-testing)
    - [Further Manual Testing](#further-manual-testing)
    - [Compatibility and Responsiveness](#compatibility-and-responsiveness)
    - [Validation](#validation)


***

## Demo
A live demo can be found - [here](https://rs87801-sportsporium.herokuapp.com/)

Main README.md file can be found - [here](https://github.com/Ranj247/sportsporium_v1/blob/main/README.md)

Project Repository can be found - [here](https://github.com/Ranj247/sportsporium_v1)


***

## Testing
### Testing User Stories
Testing User Stories from User Experience (UX) Section




### Manual Testing
Manual testing was performed on the following elements that appear across all pages on the site, to ensure that all are working as expected;

#### All Pages



### Further Manual Testing
- Checked grammar and spelling throughout document.
- Ran README text through [Online-Spellcheck](https://www.online-spellcheck.com/) to double-check on grammar and spelling.
- Ran CSS through [Autoprefixer](https://autoprefixer.github.io/) and copied the resulted CSS codes back into style.css file.

- Test carried on grounds of Performance, Accessibility, Best Practices and SEO 

- Test carried on the overall site colours on [a11y](https://color.a11y.com/), a Color Contrast Accessibility Validator.<br><br>
    

### Compatibility and Responsiveness
The website has been tested on different browsers and electronic device, no compatibility issues noted. The site was found to be fully responsive on device sizes ranging from 320px X 480px to 1920px X 1080px.

- Browsers tested:
    - Chrome 
    - Safari 
    - Firefox 

- Devices tested:
    - iPhone 6
    - Samsung A20
    - Desktop PC
    - Laptop
    - Tablet

- Test carried on the Responsiveness of all pages using [Responsive Design Checker](https://responsivedesignchecker.com/).

- Test carried on the Responsiveness of all pages using [Google Mobile-Friendly Test](https://search.google.com/test/mobile-friendly).<br><br>
    

### Validation
#### HTML
- Tested [HTML Validation](https://validator.w3.org/) No errors or warnings to show. This validator does not recognise Jinja templates & scripting, so returns errors for the lines of code where Jinja is used - this is to be expected. No errors are present in the HTML code otherwise.

#### CSS
- Tested [CSS Validation](https://jigsaw.w3.org/css-validator/) No errors found.<br><br>
    ![Image](readme-assets/images/CSS-validation-report.png)<br><br>

#### Javascript
- [JSHint](https://jshint.com/) was used to validate the JavaScript code in the script.js file. No errors are present.

#### Python
- [PEP8 Online](http://pep8online.com/) was used to validate the code in Python files.
- Expected errors were returned for the `settings.py` file:<br><br>
    ![Image](readme-assets/images/PEP8-report.png)<br><br>
    - `line too long (>79 characters)` in the `AUTH_PASSWORD_VALIDATORS = [{}]` settings x4
    - This is a known issue with the built-in Django settings, and it would not be acceptable to force a line break in the dictionary value strings.
- All other Python code is fully PEP8 compliant.

***