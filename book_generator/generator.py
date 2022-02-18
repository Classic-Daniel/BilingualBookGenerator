from ebooklib import epub
from book_generator.book_meta_data import BookMetaData

class BookGenerator:
    """
    Supported outputFormats: .epub
    """
    def createBook(self, outputPath, outputFormat, matchedSentences, bookMetaData):
        if(outputFormat == ".epub"):
            self.createEpubBook(outputPath=outputPath, matchedSentences=matchedSentences, bookMetaData=bookMetaData)
    
    def createPdfBook(self, outputPath, matchedSentences):
        pass
    
    def createEpubBook(self, outputPath, matchedSentences, bookMetaData : BookMetaData):
        book = epub.EpubBook()

        # set metadata
        # book.set_identifier('id123456')
        book.set_title(bookMetaData.title)
        book.set_language(bookMetaData.language)
        book.add_author(bookMetaData.author)

        c1 = epub.EpubHtml(title=bookMetaData.title, file_name='chap_01.xhtml', lang=bookMetaData.language)
        c1.content = f'<h1>{bookMetaData.title}</h1>'

        for sectionPairings in matchedSentences:
            c1.content = c1.content + "<p>" + sectionPairings[0] + "</p>"
            c1.content = c1.content + "<p style=\"color:gray;\">" + sectionPairings[1] + "</p>"

        # add chapter
        book.add_item(c1)

        # define Table Of Contents
        # book.toc = (epub.Link('chap_01.xhtml', 'Introduction', 'intro'),
        #             (epub.Section('Simple book'),
        #             (c1, ))
        #             )

        # add default NCX and Nav file
        book.add_item(epub.EpubNcx())
        book.add_item(epub.EpubNav())

        # define CSS style
        style = 'BODY {color: white;}'
        nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)

        # add CSS file
        book.add_item(nav_css)

        # basic spine
        book.spine = ['nav', c1]

        # write to the file
        epub.write_epub(outputPath, book, {})