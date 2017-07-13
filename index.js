'use strict';

var yaml = require('js-yaml');
var fs   = require('fs');

// Get document, or throw exception on error
try {
  var doc = yaml.safeLoad(fs.readFileSync('./resume.yaml', 'utf8'));
  //console.log(doc);
} catch (e) {
  console.log(e);
}

var jsonResume = JSON.stringify(doc);
fs.writeFileSync('./resume.json', jsonResume);
