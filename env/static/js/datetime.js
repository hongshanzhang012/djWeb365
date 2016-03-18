function toISOFormat(input)
{
    var tokens = input.split(/[ \/:.+-]/g);
    var tstring = tokens.slice(0, 3).join('-') + 'T' + tokens.slice(3, 6).join(':') + 'Z';
    return new Date(tstring);
}