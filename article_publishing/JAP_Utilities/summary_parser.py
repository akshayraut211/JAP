import docx

def get_summary_data(summaryfile):
    doc = docx.Document(summaryfile)
    file_data=[]
    summary_data=[]
    for para in doc.paragraphs:

        if para.text == '' or para.text == '\n' or para.text == ' ':

            continue
        file_data.append(para.text)
    
    for i in range(1, len(file_data),3):
        article_number_author_pre=file_data[i].split('.')
        article_number=article_number_author_pre[0]
        article_title = '.'.join(article_number_author_pre[1:])
        article_author_pre = file_data[i+1].split(' ')
        if article_author_pre[0] == 'by':
            article_author_pre.remove('by')
        article_author = ' '.join(article_author_pre).strip(' ')
        article_excerpt = file_data[i+2]
 
        summary_data.append(
                            {
                                'article_number' : article_number,
                                'article_title' : article_title,
                                'article_author' : article_author,
                                'article_excerpt' : article_excerpt
                            }
                        )      

    return summary_data

def get_general_summary(summaryfile):
    summary_data = get_summary_data(summaryfile)
    general_summary = {
                            'titles' :  [summary_data_dict['article_title'] for summary_data_dict in summary_data],
                            'authors' : [summary_data_dict['article_author'] for summary_data_dict in summary_data],
                            'excerpts' : [summary_data_dict['article_excerpt'] for summary_data_dict in summary_data]
                      }

    return general_summary

