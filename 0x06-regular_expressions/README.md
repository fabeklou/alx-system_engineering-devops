# 0x06. Regular expression

<p align="center">
    <img size="400" src="https://www.alura.com.br/artigos/assets/principais-casos-uso-regex-para-tratamento-dados/principais-casos-uso-regex-para-tratamento-dados.png">
</p>

## Background Context

For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the `//`:

```bash
sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
fabeklou@ubuntu$
fabeklou@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
fabeklou@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
fabeklou@ubuntu$ ./example.rb 127.0.0.a
```

## Resources

Read or watch:

- [Regular expressions - basics](https://www.slideshare.net/neha_jain/introducing-regular-expressions)
- [Regular expressions - advanced](https://www.slideshare.net/neha_jain/advanced-regular-expressions-80296518)
- [Rubular is your best friend](https://rubular.com/)
- [Use a regular expression against a problem: now you have 2 problems](https://blog.codinghorror.com/regular-expressions-now-you-have-two-problems/)
- [Learn Regular Expressions with simple, interactive exercises](https://regexone.com/)
