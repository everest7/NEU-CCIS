package Strategy;

import java.util.List;
import java.util.function.Supplier;
import org.w3c.dom.Text;

enum OutputFormat {MARKDOWN, HTML}

interface ListStrategy {
  // make start(), end() default since markdown doesn't need these two methods
  default void start(StringBuilder sb) {}
  void addListItem(StringBuilder sb, String item);
  default void end(StringBuilder sb) {}
}

class MarkdownListStrategy implements ListStrategy {

  @Override
  public void addListItem(StringBuilder sb, String item) {
    sb.append(" * ").append(item)
        .append(System.lineSeparator());
  }
}

class HtmlListStrategy implements ListStrategy {

  @Override
  public void start(StringBuilder sb) {
    sb.append("<ul>").append(System.lineSeparator());
  }

  @Override
  public void addListItem(StringBuilder sb, String item) {
    sb.append(" <li>")
        .append(item)
        .append("</li>")
        .append(System.lineSeparator());
  }

  @Override
  public void end(StringBuilder sb) {
    sb.append("</ul>").append(System.lineSeparator());
  }
}

class TextProcessor<LS extends ListStrategy> {
  private StringBuilder sb = new StringBuilder();
  private ListStrategy listStrategy;

  // declare the constructor statically
//  public TextProcessor(Supplier<? extends LS> ctor) {
//    listStrategy = ctor.get();
//  }

  public TextProcessor(OutputFormat format) {
    setOutputFormat(format);
  }

  public void  setOutputFormat(OutputFormat format) {
    switch (format) {
      case MARKDOWN:
        listStrategy = new MarkdownListStrategy();
        break;
      case HTML:
        listStrategy = new HtmlListStrategy();
        break;
    }
  }

  public void appendList(List<String> items) {
    listStrategy.start(sb);
    for (String s : items) {
      listStrategy.addListItem(sb, s);
    }
    listStrategy.end(sb);
  }

  public void clear() {
    sb.setLength(0);
  }

  @Override
  public String toString() {
    return sb.toString();
  }
}

public class Strategy {

  public static void main(String[] args) {
    // dynamic approach
    TextProcessor tp = new TextProcessor(OutputFormat.MARKDOWN);
    tp.appendList(List.of("liberte", "egalite", "fraternite"));
    System.out.println(tp);

    tp.clear();
    tp.setOutputFormat(OutputFormat.HTML);
    tp.appendList(List.of("Inheritance", "encapsulate", "polymorphism"));
    System.out.println(tp);

    // static approach
//    TextProcessor<MarkdownListStrategy> tp = new TextProcessor<MarkdownListStrategy>(MarkdownListStrategy::new);

  }
}
