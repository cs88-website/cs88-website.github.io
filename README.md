# DATA C88C Webaite

## [https://c88c.org](https://c88c.org)
## [~https://cs88.org~](https://cs88.org)

This site exists _solely_ to redirect to the current semester's site, or pages.
It may contain redirects for as many "generic" assignments, resources, etc. as necessary.

### Directions

* Create a new repository for each semester, under this organization.
* Update the index.html file to point to the new repo.
* Use the following:
    * faXX for Fall semesters
    * spXX for Spring semesters
    * suXX for Summer semesters
* In this repo: find-and-replace all semester redirects
    * e.g. replace "fa23" with "sp24"
    * or run `ruby script/create_redirects.rb`

## Redirect Pages

* The regular website uses the scheme `/[semester]/lab/labXX`
* Inside [`pages/`](pages/) there are files which create a redirect
* You can regenerate these easily by running `ruby script/create_redirects.rb`
