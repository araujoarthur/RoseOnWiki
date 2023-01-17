document.addEventListener('DOMContentLoaded', function(){
    guiaButton = document.querySelector('#guiaButton');
    questButton = document.querySelector('#questButton');
    npcButton = document.querySelector('#npcButton');
    itemButton = document.querySelector('#itemButton');

    sendGuiaButton = document.querySelector('#createGuidePage');
    sendQuestButton = document.querySelector('#createQuestPage');
    sendNpcButton = document.querySelector('#createNPCPage');
    sendItemButton = document.querySelector('#createItemPage');

    guiaSection = document.querySelector("#guiaSection");
    questSection = document.querySelector("#questSection");
    npcSection = document.querySelector("#npcSection");
    itemSection = document.querySelector("#itemSection");

    let editorGuia = undefined;
    let editorNPC = undefined;
    let editorQuest = undefined;
    let editorItem = undefined;

    /* To Do:
        Build Up Items/NPC and Guide Forms and Database.
        Build Up AJAX Fetch for inserting pages into db.
        Searching pages.

    */

    guiaButton.addEventListener('click', function(){
        questSection.classList.remove('block');
        npcSection.classList.remove('block');
        itemSection.classList.remove('block');

        questSection.classList.add('hidden');
        npcSection.classList.add('hidden');
        itemSection.classList.add('hidden');

        guiaSection.classList.add('block');
        guiaSection.classList.remove('hidden');
        
        if (editorGuia == undefined){
            editorGuia = new EditorJS({
                holder:'textAreaGuia',
                placeholder:'Texto do Guia',
                minHeight:300,
                tools: {
                    image: SimpleImage,
                    header:{
                        class: Header,
                        config: {
                          placeholder: 'Enter a header',
                          levels: [2, 3, 4],
                          defaultLevel: 3
                        }
                    },
                    linkTool: {
                        class: LinkTool,
                        config: {
                          endpoint: '/fetchUrl', // Your backend endpoint for url data fetching,
                        }
                    },
                    raw: RawTool,
                    list: {
                        class: List,
                        inlineToolbar: true,
                        config: {
                          defaultStyle: 'unordered'
                        }
                    },
                    quote:Quote,
                    delimiter: Delimiter,
                    hyperlink: {
                        class: Hyperlink,
                        config: {
                          shortcut: 'CMD+L',
                          target: '_blank',
                          rel: 'nofollow',
                          availableTargets: ['_blank', '_self'],
                          availableRels: ['author', 'noreferrer'],
                          validate: false,
                        }
                    },
                    warning: {
                        class: Warning,
                        inlineToolbar: true,
                        shortcut: 'CMD+SHIFT+W',
                        config: {
                          titlePlaceholder: 'Title',
                          messagePlaceholder: 'Message',
                        },
                    },
                    
                    
                },
                i18n: {
                    /**
                     * @type {I18nDictionary}
                     */
                    messages: {
                      /**
                       * Other below: translation of different UI components of the editor.js core
                       */
                      ui: {
                        "blockTunes": {
                          "toggler": {
                            "Click to tune": "Clique para modificar",
                            "or drag to move": "ou Arraste para mover"
                          },
                        },
                        "inlineToolbar": {
                          "converter": {
                            "Convert to": "Converter para"
                          }
                        },
                        "toolbar": {
                          "toolbox": {
                            "Add": "Adicionar"
                          }
                        }
                      },
                  
                      /**
                       * Section for translation Tool Names: both block and inline tools
                       */
                      toolNames: {
                        "Text": "Texto",
                        "Heading": "Cabeçalho",
                        "List": "Lista",
                        "Quote": "Citação",
                        "Delimiter": "Delimitador",
                        "Raw HTML": "HTML Puro",
                        "Table": "Tabela",
                        "Link": "Link",
                        "Marker": "Marcador",
                        "Bold": "Negrito",
                        "Italic": "Itálico",
                        "InlineCode": "Codigo Inline",
                        "Warning": "Aviso"
                      },
                  
                      /**
                       * Section for passing translations to the external tools classes
                       */
                      tools: {
                        /**
                         * Each subsection is the i18n dictionary that will be passed to the corresponded plugin
                         * The name of a plugin should be equal the name you specify in the 'tool' section for that plugin
                         */
                        "warning": { // <-- 'Warning' tool will accept this dictionary section
                          "Title": "Titulo",
                          "Message": "Mensagem",
                        },
                  
                        /**
                         * Link is the internal Inline Tool
                         */
                        "link": {
                          "Add a link": "Adicione um Link"
                        },
                        /**
                         * The "stub" is an internal block tool, used to fit blocks that does not have the corresponded plugin
                         */
                        "stub": {
                          'The block can not be displayed correctly.': 'O bloco não pode ser mostrado corretamente'
                        }
                      },
                  
                      /**
                       * Section allows to translate Block Tunes
                       */
                      blockTunes: {
                        /**
                         * Each subsection is the i18n dictionary that will be passed to the corresponded Block Tune plugin
                         * The name of a plugin should be equal the name you specify in the 'tunes' section for that plugin
                         *
                         * Also, there are few internal block tunes: "delete", "moveUp" and "moveDown"
                         */
                        "delete": {
                          "Delete": "Deletar"
                        },
                        "moveUp": {
                          "Move up": "Mover para cima"
                        },
                        "moveDown": {
                          "Move down": "Mover para baixo"
                        }
                      },
                    }
                  },
            });    
        }

    

    });

    questButton.addEventListener('click', function(){
        guiaSection.classList.remove('block');
        npcSection.classList.remove('block');
        itemSection.classList.remove('block');

        guiaSection.classList.add('hidden');
        npcSection.classList.add('hidden');
        itemSection.classList.add('hidden');

        questSection.classList.add('block');
        questSection.classList.remove('hidden');

        if (editorQuest == undefined){
            editorQuest = new EditorJS({
                holder:'textAreaQuest',
                placeholder:'Texto da Quest',
                minHeight:300,
                tools: {
                    image: SimpleImage,
                    header:{
                        class: Header,
                        config: {
                        placeholder: 'Enter a header',
                        levels: [2, 3, 4],
                        defaultLevel: 3
                        }
                    },
                    linkTool: {
                        class: LinkTool,
                        config: {
                        endpoint: '/fetchUrl', // Your backend endpoint for url data fetching,
                        }
                    },
                    raw: RawTool,
                    list: {
                        class: List,
                        inlineToolbar: true,
                        config: {
                        defaultStyle: 'unordered'
                        }
                    },
                    quote:Quote,
                    delimiter: Delimiter,
                    hyperlink: {
                        class: Hyperlink,
                        config: {
                        shortcut: 'CMD+L',
                        target: '_blank',
                        rel: 'nofollow',
                        availableTargets: ['_blank', '_self'],
                        availableRels: ['author', 'noreferrer'],
                        validate: false,
                        }
                    },
                    warning: {
                        class: Warning,
                        inlineToolbar: true,
                        shortcut: 'CMD+SHIFT+W',
                        config: {
                        titlePlaceholder: 'Title',
                        messagePlaceholder: 'Message',
                        },
                    },
                    
                    
                },
                i18n: {
                    /**
                     * @type {I18nDictionary}
                     */
                    messages: {
                    /**
                     * Other below: translation of different UI components of the editor.js core
                     */
                    ui: {
                        "blockTunes": {
                        "toggler": {
                            "Click to tune": "Clique para modificar",
                            "or drag to move": "ou Arraste para mover"
                        },
                        },
                        "inlineToolbar": {
                        "converter": {
                            "Convert to": "Converter para"
                        }
                        },
                        "toolbar": {
                        "toolbox": {
                            "Add": "Adicionar"
                        }
                        }
                    },
                
                    /**
                     * Section for translation Tool Names: both block and inline tools
                     */
                    toolNames: {
                        "Text": "Texto",
                        "Heading": "Cabeçalho",
                        "List": "Lista",
                        "Quote": "Citação",
                        "Delimiter": "Delimitador",
                        "Raw HTML": "HTML Puro",
                        "Table": "Tabela",
                        "Link": "Link",
                        "Marker": "Marcador",
                        "Bold": "Negrito",
                        "Italic": "Itálico",
                        "InlineCode": "Codigo Inline",
                        "Warning": "Aviso"
                    },
                
                    /**
                     * Section for passing translations to the external tools classes
                     */
                    tools: {
                        /**
                         * Each subsection is the i18n dictionary that will be passed to the corresponded plugin
                         * The name of a plugin should be equal the name you specify in the 'tool' section for that plugin
                         */
                        "warning": { // <-- 'Warning' tool will accept this dictionary section
                        "Title": "Titulo",
                        "Message": "Mensagem",
                        },
                
                        /**
                         * Link is the internal Inline Tool
                         */
                        "link": {
                        "Add a link": "Adicione um Link"
                        },
                        /**
                         * The "stub" is an internal block tool, used to fit blocks that does not have the corresponded plugin
                         */
                        "stub": {
                        'The block can not be displayed correctly.': 'O bloco não pode ser mostrado corretamente'
                        }
                    },
                
                    /**
                     * Section allows to translate Block Tunes
                     */
                    blockTunes: {
                        /**
                         * Each subsection is the i18n dictionary that will be passed to the corresponded Block Tune plugin
                         * The name of a plugin should be equal the name you specify in the 'tunes' section for that plugin
                         *
                         * Also, there are few internal block tunes: "delete", "moveUp" and "moveDown"
                         */
                        "delete": {
                        "Delete": "Deletar"
                        },
                        "moveUp": {
                        "Move up": "Mover para cima"
                        },
                        "moveDown": {
                        "Move down": "Mover para baixo"
                        }
                    },
                    }
                },
            });
        }
        

    });

    npcButton.addEventListener('click', function(){
        guiaSection.classList.remove('block');
        questSection.classList.remove('block');
        itemSection.classList.remove('block');

        guiaSection.classList.add('hidden');
        questSection.classList.add('hidden');
        itemSection.classList.add('hidden');

        npcSection.classList.add('block');
        npcSection.classList.remove('hidden');

        if (editorNPC == undefined){
            editorNPC = new EditorJS({
                holder:'textAreaNPC',
                placeholder:'Texto do NPC',
                minHeight:300,
                tools: {
                    image: SimpleImage,
                    header:{
                        class: Header,
                        config: {
                          placeholder: 'Enter a header',
                          levels: [2, 3, 4],
                          defaultLevel: 3
                        }
                    },
                    linkTool: {
                        class: LinkTool,
                        config: {
                          endpoint: '/fetchUrl', // Your backend endpoint for url data fetching,
                        }
                    },
                    raw: RawTool,
                    list: {
                        class: List,
                        inlineToolbar: true,
                        config: {
                          defaultStyle: 'unordered'
                        }
                    },
                    quote:Quote,
                    delimiter: Delimiter,
                    hyperlink: {
                        class: Hyperlink,
                        config: {
                          shortcut: 'CMD+L',
                          target: '_blank',
                          rel: 'nofollow',
                          availableTargets: ['_blank', '_self'],
                          availableRels: ['author', 'noreferrer'],
                          validate: false,
                        }
                    },
                    warning: {
                        class: Warning,
                        inlineToolbar: true,
                        shortcut: 'CMD+SHIFT+W',
                        config: {
                          titlePlaceholder: 'Title',
                          messagePlaceholder: 'Message',
                        },
                    },
                    
                    
                },
                i18n: {
                    /**
                     * @type {I18nDictionary}
                     */
                    messages: {
                      /**
                       * Other below: translation of different UI components of the editor.js core
                       */
                      ui: {
                        "blockTunes": {
                          "toggler": {
                            "Click to tune": "Clique para modificar",
                            "or drag to move": "ou Arraste para mover"
                          },
                        },
                        "inlineToolbar": {
                          "converter": {
                            "Convert to": "Converter para"
                          }
                        },
                        "toolbar": {
                          "toolbox": {
                            "Add": "Adicionar"
                          }
                        }
                      },
                  
                      /**
                       * Section for translation Tool Names: both block and inline tools
                       */
                      toolNames: {
                        "Text": "Texto",
                        "Heading": "Cabeçalho",
                        "List": "Lista",
                        "Quote": "Citação",
                        "Delimiter": "Delimitador",
                        "Raw HTML": "HTML Puro",
                        "Table": "Tabela",
                        "Link": "Link",
                        "Marker": "Marcador",
                        "Bold": "Negrito",
                        "Italic": "Itálico",
                        "InlineCode": "Codigo Inline",
                        "Warning": "Aviso"
                      },
                  
                      /**
                       * Section for passing translations to the external tools classes
                       */
                      tools: {
                        /**
                         * Each subsection is the i18n dictionary that will be passed to the corresponded plugin
                         * The name of a plugin should be equal the name you specify in the 'tool' section for that plugin
                         */
                        "warning": { // <-- 'Warning' tool will accept this dictionary section
                          "Title": "Titulo",
                          "Message": "Mensagem",
                        },
                  
                        /**
                         * Link is the internal Inline Tool
                         */
                        "link": {
                          "Add a link": "Adicione um Link"
                        },
                        /**
                         * The "stub" is an internal block tool, used to fit blocks that does not have the corresponded plugin
                         */
                        "stub": {
                          'The block can not be displayed correctly.': 'O bloco não pode ser mostrado corretamente'
                        }
                      },
                  
                      /**
                       * Section allows to translate Block Tunes
                       */
                      blockTunes: {
                        /**
                         * Each subsection is the i18n dictionary that will be passed to the corresponded Block Tune plugin
                         * The name of a plugin should be equal the name you specify in the 'tunes' section for that plugin
                         *
                         * Also, there are few internal block tunes: "delete", "moveUp" and "moveDown"
                         */
                        "delete": {
                          "Delete": "Deletar"
                        },
                        "moveUp": {
                          "Move up": "Mover para cima"
                        },
                        "moveDown": {
                          "Move down": "Mover para baixo"
                        }
                      },
                    }
                  },
            });
        }
        
    });

    itemButton.addEventListener('click', function(){
        guiaSection.classList.remove('block');
        questSection.classList.remove('block');
        npcSection.classList.remove('block');

        guiaSection.classList.add('hidden');
        questSection.classList.add('hidden');
        npcSection.classList.add('hidden');

        itemSection.classList.add('block');
        itemSection.classList.remove('hidden');

        if (editorItem == undefined){
            editorItem = new EditorJS({
                holder:'textAreaItem',
                placeholder:'Texto do Item',
                minHeight:300,
                tools: {
                    image: SimpleImage,
                    header:{
                        class: Header,
                        config: {
                          placeholder: 'Enter a header',
                          levels: [2, 3, 4],
                          defaultLevel: 3
                        }
                    },
                    linkTool: {
                        class: LinkTool,
                        config: {
                          endpoint: '/fetchUrl', // Your backend endpoint for url data fetching,
                        }
                    },
                    raw: RawTool,
                    list: {
                        class: List,
                        inlineToolbar: true,
                        config: {
                          defaultStyle: 'unordered'
                        }
                    },
                    quote:Quote,
                    delimiter: Delimiter,
                    hyperlink: {
                        class: Hyperlink,
                        config: {
                          shortcut: 'CMD+L',
                          target: '_blank',
                          rel: 'nofollow',
                          availableTargets: ['_blank', '_self'],
                          availableRels: ['author', 'noreferrer'],
                          validate: false,
                        }
                    },
                    warning: {
                        class: Warning,
                        inlineToolbar: true,
                        shortcut: 'CMD+SHIFT+W',
                        config: {
                          titlePlaceholder: 'Title',
                          messagePlaceholder: 'Message',
                        },
                    },
                    
                    
                },
                i18n: {
                    /**
                     * @type {I18nDictionary}
                     */
                    messages: {
                      /**
                       * Other below: translation of different UI components of the editor.js core
                       */
                      ui: {
                        "blockTunes": {
                          "toggler": {
                            "Click to tune": "Clique para modificar",
                            "or drag to move": "ou Arraste para mover"
                          },
                        },
                        "inlineToolbar": {
                          "converter": {
                            "Convert to": "Converter para"
                          }
                        },
                        "toolbar": {
                          "toolbox": {
                            "Add": "Adicionar"
                          }
                        }
                      },
                  
                      /**
                       * Section for translation Tool Names: both block and inline tools
                       */
                      toolNames: {
                        "Text": "Texto",
                        "Heading": "Cabeçalho",
                        "List": "Lista",
                        "Quote": "Citação",
                        "Delimiter": "Delimitador",
                        "Raw HTML": "HTML Puro",
                        "Table": "Tabela",
                        "Link": "Link",
                        "Marker": "Marcador",
                        "Bold": "Negrito",
                        "Italic": "Itálico",
                        "InlineCode": "Codigo Inline",
                        "Warning": "Aviso"
                      },
                  
                      /**
                       * Section for passing translations to the external tools classes
                       */
                      tools: {
                        /**
                         * Each subsection is the i18n dictionary that will be passed to the corresponded plugin
                         * The name of a plugin should be equal the name you specify in the 'tool' section for that plugin
                         */
                        "warning": { // <-- 'Warning' tool will accept this dictionary section
                          "Title": "Titulo",
                          "Message": "Mensagem",
                        },
                  
                        /**
                         * Link is the internal Inline Tool
                         */
                        "link": {
                          "Add a link": "Adicione um Link"
                        },
                        /**
                         * The "stub" is an internal block tool, used to fit blocks that does not have the corresponded plugin
                         */
                        "stub": {
                          'The block can not be displayed correctly.': 'O bloco não pode ser mostrado corretamente'
                        }
                      },
                  
                      /**
                       * Section allows to translate Block Tunes
                       */
                      blockTunes: {
                        /**
                         * Each subsection is the i18n dictionary that will be passed to the corresponded Block Tune plugin
                         * The name of a plugin should be equal the name you specify in the 'tunes' section for that plugin
                         *
                         * Also, there are few internal block tunes: "delete", "moveUp" and "moveDown"
                         */
                        "delete": {
                          "Delete": "Deletar"
                        },
                        "moveUp": {
                          "Move up": "Mover para cima"
                        },
                        "moveDown": {
                          "Move down": "Mover para baixo"
                        }
                      },
                    }
                  },
            });
        }

        selectItemTypes = document.querySelector('#item_types')
        fetch('/api/getItemTypes').then((response) => response.json()).then((data) => {
            for(let item of data){
                let opt = document.createElement('option');
                opt.value = item.id;
                opt.innerHTML = item.name;
                opt.classList.add('capitalize');
                selectItemTypes.appendChild(opt);
            }
        });

        selectItemSubtypes = document.querySelector('#item_subtypes');

        selectItemTypes.addEventListener('change', () => {
            /* Lembrar de retirar itens dos inputs que vem depois desse em caso de mudança. */
            fetch('/api/getItemSubtypes?item_type='+selectItemTypes.value).then((response) => response.json()).then((data) =>{
                selectItemSubtypes.innerHTML = ''
                for(let item of data){
                    let opt = document.createElement('option');
                    opt.value = item.id;
                    opt.innerHTML = item.name;
                    opt.classList.add('capitalize');
                    selectItemSubtypes.appendChild(opt);
                } 
            });
        });

        selectItemTypes.addEventListener('change', async function() {
            async function getStatus(){
                const respons = await fetch('/api/getStatusTypes');
                let jsonObj = await respons.json();

                return jsonObj;
            }

            async function getFields(id){
                const respons = await fetch('/api/getFieldsItemType?id='+id);
                let jsonObj = await respons.json();

                return jsonObj; 
            }

            let fields = await getFields(selectItemTypes.value);
            alert(JSON.stringify(fields))
        });

    });
});

